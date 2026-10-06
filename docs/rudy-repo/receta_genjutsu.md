# Receta de Genjutsu y lecciones aprendidas

Modelo: `generate_video` con `model: "hf_mult_replace_object"`. El video fuente va como `video`. Las imágenes van en `medias`, y se citan en el prompt como "reference image N", donde N es su orden.

## Estructura del prompt que funciona

Los prompts exactos están en `prompts/genjutsu_felipe_2.0.md`. El orden de cada envío:

1. **"NO text, NO subtitles, NO captions"** siempre va como **punto 1**. Si se pide al final, Genjutsu quema subtítulos inventados al azar (transcribe el audio).
2. **Encuadre:** "keep exactly the same close framing, do NOT zoom out". Solo pedir objetos que salen en cuadro. Si pides reemplazar algo que no se ve, abre el plano a cuerpo completo.
3. **Proporciones y altura de las manos**, en % del cuadro medido del original: "hands must NOT drop to stomach".
4. **"Replace the microphone with the flashlight from reference image 2/3"**, sin describir el micrófono (pedido de Liz).
5. **Personaje:** "the man from reference image 1". Describir solo lo que es: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; dark green shirt open over a white t-shirt.
6. **Reloj:** "brown leather strap watch on HIS LEFT wrist, which appears on the RIGHT side of the image; the other wrist has NO watch".
7. **Luz:**
   - cuarto negro, la linterna es la única fuente: "ONLY light source… no key/fill/side light";
   - luz desde abajo como en reference image 4;
   - **HARD, high-contrast, dark band across forehead, NOT soft, NOT flat**;
   - cuerpo muy oscuro: "only his hands catch a faint glow".
8. **Si no hay evento de luz:** "the flashlight is ALREADY ON from the very first frame and never turns on again".

## Lecciones

### Tiempos de un evento

**No obedece segundos con decimales.**

- Pedí el encendido en "0.45 s" y lo puso en el 4.42 s.
- En la prueba del clip 8, los spots que pedí "para el segundo 3" se prendieron en el 8.85 s.

**Sí obedece tiempos anclados a palabras o acciones.**

- "at the very beginning, before his first word, ON for almost the entire video" dio un encendido en el 0.79 s.
- Sí respeta "turns ON INSTANTLY, NOT a slow fade-in": el cambio toma 2 o 3 cuadros.
- Tiende a poner los eventos **tarde**.

### Luz consistente entre tomas

- Usar como referencia 4 un **cuadro de una toma ya aprobada** (`refs/ref_luz_clip1_v3.png`).
- Quitar la palabra "soft" y pedir luz dura.
- "soft, well exposed, not blown out" evita caras quemadas, pero aplana la luz. Liz rechazó así el 5+7.
- Los ojos casi nunca quedan en sombra, aunque se pida: es un límite del modelo.

### Agrupar tomas

- Higgsfield rechaza clips de menos de 2 s. Se juntan varias tomas en un solo envío (concat con ffmpeg y rutas absolutas en el archivo de lista).
- Si **una** toma del envío tiene un evento de luz (encendido), Genjutsu aplica el terror solo a esa y "normaliza" las demás con luz de estudio. **El clip con encendido va solo.**
- Las tomas con la linterna prendida desde el inicio sí se pueden juntar.

### Límites

- Acepta clips de **14.3 s**.
- **Rechaza 48 s con error 422** y menos de 2 s.
- `get_cost` no avisa del límite de duración: cotiza 30 s sin quejarse.

### Salida

- Sale en 720x1280 o 728x1264, a 24 fps.
- Recorta unos 0.3 s del final.
- Conserva el audio original alineado.
- Tarda unos 10 minutos o más por cada 5 s de clip.

### Fallas recurrentes

- **Accesorios:**
  - no quita el anillo aunque se le pida (por eso se queda);
  - a veces pierde el reloj (clip 3) o lo pone en la muñeca equivocada si no se dice "RIGHT side of the image".
- **Silla blanca:**
  - la quita de forma inconsistente (en la prueba a 480p sí, en el 720p no);
  - se borra en edición con `quitar_silla*.py`.
- **Ropa y texto:**
  - el texto de letreros de la referencia sale ilegible;
  - aparece una etiqueta blanca chica en el borde de la camisa.
- **Pedidos que confunden:**
  - mencionar "gray hair", aunque sea en negativo, confunde al modelo: no hacerlo;
  - si se menciona el pantalón y no sale en cuadro, abre el plano.
- **Presets:** sugiere presets ("IN THE DARK", "Earth zoom out"). Hay que pasar `declined_preset_id`.

## Subir archivos

1. `media_upload` da una URL firmada.
2. `curl -X PUT --upload-file archivo.mp4 "<url>"`.
3. `media_confirm`.

Para cotizar con `get_cost` hace falta subir el video primero.

## Edición fuera de Genjutsu (scripts en `archivos/`)

- **`quitar_silla.py` / `quitar_silla_clip8.py`:**
  - trabaja en YUV444;
  - detecta el asiento blanco (Y > 180, croma neutro) en los 140 px de abajo a la izquierda;
  - aplica una envolvente temporal max/min;
  - rellena con piso desplazado desde la derecha, con máscara difuminada.
- **`corregir_lente.py`:**
  - compensa el brinco del cambio de lente del iPhone en el outro (escala, desplazamiento y brillo);
  - lo suelta en unos 1 s.
- **`clip1_luz_edicion.py` / `luz_post.py`:** plan B de encendido y viñeteo en edición. Liz prefirió el encendido de Genjutsu.
- **Medir la luz:** `ffmpeg -vf signalstats` + YAVG por cuadro. Para el inicio del habla: `silencedetect`.

## Retoque de la referencia (ceja)

- Se pasa nano banana pro sobre un recorte de la cara. El resultado regresa alineado al píxel.
- Se pega **solo un parche elíptico difuminado** sobre la hoja: centro (650,532) en el recorte, ejes 85×58, blur 14.
- Liz lo terminó en Photoshop.
