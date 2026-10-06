# Estado y pendientes (al 5 oct 2026)

## Felipe 2.0: estado por clip

| Clips | Job | Resultado | Estado |
|---|---|---|---|
| 1 | `f67f6dd8-39c7-4e30-b470-e9758ad5d16c` | `clip_1_genjutsu_720p_v3.mp4` | ✅ **Aprobado** ("sin viñeteo") |
| 2+4+6 | `d2894c4a-9fe2-4aab-85e6-68ae784999f4` | `clips_2_4_6_genjutsu_720p.mp4` | ⏳ Sin respuesta de Liz |
| 3 | `012981eb-fbef-458f-9bd5-0b1dfe056fa9` | `clip_3_genjutsu_720p.mp4` | ⚠️ Le falta el reloj |
| 5+7 | `35ed4e03-0320-4d93-af9c-a1e6fd0fd24c` | `clips_5_7_genjutsu_720p_v3.mp4` | ⏳ Falta el OK |
| 8 | `999e9363-d0f0-407a-9109-de9bbab1dc4e` | `clip_8_genjutsu_720p_sin_silla.mp4` | ✅ Liz eligió la versión normal |

Todo está en `archivos/02_felipe-juarez-2.0/genjutsu/`.

### Clip 1

- Se prende en el 0.79 s, en 3 cuadros, antes de la primera palabra (1.17 s), y se queda prendido todo el clip.
- El reloj sale a la derecha y la piel queda limpia.
- **Contras:**
  - los ojos quedan iluminados;
  - la camisa verde todavía se ve;
  - el encuadre es un poco más abierto;
  - no se ve el gesto del pulgar.

### Clips 2+4+6

- La cara de Felipe 2.0 sale consistente y el reloj está bien.
- **Fallas:**
  - la luz es más frontal y pareja que en el resto, y la camisa verde se ve;
  - el pantalón sale gris azulado en el detalle de la mano.
- Se hizo antes de descubrir la receta de luz dura. Si Liz lo rechaza, se rehace con la ref `refs/ref_luz_clip1_v3.png`: 6.0 s ≈ 49 cr.

### Clip 3

- La luz dura es igual a la del clip 1, la linterna queda prendida todo el tiempo y las manos están frente al pecho.
- **Sin reloj en ninguna muñeca.** También hay una etiqueta blanca de la camisa abajo a la izquierda.
- **Opciones:**
  1. agregar el reloj en edición (gratis; antes se le enseña una prueba a Liz);
  2. reenviar (84 cr).

### Clips 5+7

- Hay franja de sombra en la frente y sombra de nariz, igual que en el clip 1.
- La linterna queda prendida todo el tiempo y el reloj sale a la derecha.
- Los ojos no quedan en sombra: es un límite de Genjutsu.

### Clip 8

- Spots encendidos todo el tiempo, reloj a la derecha y cejas limpias.
- Genjutsu dejó la silla blanca (desde el 3.88 s). Se borró con `quitar_silla_clip8.py`.
- El letrero real del showroom ("Creamos soluciones inmobiliarias…") sale como texto ilegible en la pared. Se puede difuminar si Liz lo pide.

## Decisiones abiertas

1. Reloj del clip 3: arreglarlo en edición o reenviar.
2. Aprobación del 5+7 v3.
3. Aprobación del 2+4+6, o rehacerlo con la receta de luz dura.
4. Voz: **Jonas – Mexican** contra **Arturo Casares**, la del primer corte. Ver `voz_elevenlabs.md`.
5. Opcional: difuminar el texto ilegible de la pared en el clip 8.
6. Armar el video final con Felipe 2.0. Liz armó el del primer corte ella misma.

## Felipe 1.0 (primer corte, cerrado)

El video final lo armó Liz:

- `Clip Original.mp4`
- `Clip Voz.mp4`
- `Video FInal Solo Voz.mp4`
- con voz: `01_felipe-juarez-1.0_voz/Video Final Voz Arturo Casares.mp4`

Todo es 720x1248, 24 fps, 42.5 s. Hay una comparativa de referencia en `01_felipe-juarez-1.0_genjutsu/Comparativa Final.mp4`. La nota original menciona `comparativa_original_vs_clip_voz.mp4`, pero ese archivo ya no existe en Downloads.
