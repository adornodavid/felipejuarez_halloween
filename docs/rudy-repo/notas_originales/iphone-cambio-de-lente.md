---
name: iphone-cambio-de-lente
description: Cómo quitar el brinco cuando el iPhone cambia de lente a media toma (dolly/zoom) — compensar y soltar en ~1 s; trampas de color de ffmpeg
metadata:
  type: reference
---

Caso: "Outro TerraRegia.mp4" (30 sep 2026), brinco en el cuadro 62 (2.07 s) al abrirse la cámara: escala 0.966 vs 0.991 normal, +31 px en y, +5 % de brillo.

**Método que funcionó** (script `~/Downloads/CLAUDE/terraregia-genjutsu-prueba/corregir_lente.py`):
1. ORB + estimateAffinePartial2D entre cuadro 61→62 (salto) y el promedio 60→61 / 62→63 (movimiento normal). Corrección C = M_normal · M_salto⁻¹.
2. Aplicar C desde el cuadro del salto y soltarla a identidad en ~36 cuadros con smoothstep; como la cámara ya se mueve, el ajuste se esconde. Borde por BORDER_REFLECT (en chroma no se ve). NO meter zoom extra por cuadro: crea su propio brinco.
3. Brillo: ganancia SOLO de luma. Una ganancia por canal medida en todo el cuadro se sesga con el fondo verde y tiñe de cian lo blanco.

**Trampas de ffmpeg:** trabajar en yuv444p con conversión BT.709 propia (ida y vuelta exacta). Las banderas -colorspace/-color_range como opción de SALIDA disparan una conversión que aclara todo ~9 niveles de Y; van como opción de ENTRADA del rawvideo. Verificar que un cuadro no tocado tenga la misma YAVG que el original.
