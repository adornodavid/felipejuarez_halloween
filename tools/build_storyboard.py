#!/usr/bin/env python3
"""Genera build/sb/storyboard.html (artifact) del Episodio 1 «Miedo a invertir» con cuadros embebidos.
Regla de David: storyboard aprobado antes de la Versión 1. Las notas y aprobaciones se guardan con la capacidad `db`.
Uso: python3 tools/build_storyboard.py [ruta_clip_lipsync_540.mp4]
"""
import base64, json, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SB = f"{R}/build/sb"
def b64(p):
    with open(p, "rb") as f: return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
def pair(n):
    import glob; return b64(glob.glob(f"{SB}/frames/pair_{n:02d}_*.jpg")[0])
LIPSYNC = sys.argv[1] if len(sys.argv) > 1 else None

# ---------- escenas (tiempos = lo que David DIJO, david_words.json) ----------
SC = [
 dict(id="intro", n="00", t="0 – 6 s", title="Intro · ¿Le temes a invertir?", frames=None, intro=True,
      plano="Animación existente (cerillo que se enciende, 1080×1920, 24 fps, 10 s). Propuesta: recortarla a 6 s (del raspón del cerillo al texto completo) para que el video total quede en ≈52 s.",
      luz="La llama es la única luz: cálida ≈2200 K, parpadeo real. Al apagarse el cerillo → negro total que enlaza con el clip 1.",
      motor="Ya existe (Rudy). Solo corte + sonido. 0 cr.",
      sub="Sin subtítulo (el texto ya está en la animación).",
      son="SFX raspón de cerillo + chisporroteo · room tone grave · la música entra con el primer plano de Felipe, no antes."),
 dict(id="c1", n="01", t="1.2 – 6.3 s", title="Clip 1 · «Vio el terreno, le gustó. Dijo: lo pienso, te aviso»", frames=2, test=True,
      plano="Close-up frontal, pecho-arriba, mismo encuadre y pose de David. Primer cuadro en NEGRO; 3 cuadros antes de la primera palabra la linterna se enciende de golpe (clic), no fade.",
      luz="Linterna como ÚNICA fuente, desde abajo del mentón, dura, ratio cara 1 : cuerpo 0.05, ≈4000 K, franja de sombra en la frente, sombra de nariz hacia arriba. Fondo negro puro.",
      motor="Still Nano Banana Pro (ficha + luz dura) ✅ hecho → Kling 3.0 Motion Control 1080p con tu actuación como driver (≈15 cr HF) → Lipsync 2.0 en recorte de cara con la voz Jonas (≈420 cr/s Magnific). El encendido se hace en edición (negro + flash 3 cuadros + sonido).",
      sub="«Vio el terreno, le gustó.» / «Dijo: lo pienso, te aviso.» — una línea, centrada abajo, blanca, serif cinematográfica, entra y sale con la frase.",
      son="Clic de linterna (seco) · drone grave arranca · voz Jonas."),
 dict(id="c2", n="02", t="7.1 – 7.9 s", title="Clip 2 · «Nunca me avisó» (perfil)", frames=3,
      plano="Close-up de lado (tu clip 2, 1.9 s). Corte seco desde el frontal: el cambio de ángulo es el primer momento cinematográfico.",
      luz="Misma linterna, ahora desde abajo-lateral: la mitad de la cara en sombra total. Referencia: el cuadro de la derecha (Rudy) ya lo logra.",
      motor="Still de perfil (Nano Banana con el cuadro de perfil + ficha) → Kling MC → Lipsync 2.0. Clips de 2 s: se mandan solos, Kling no tiene mínimo.",
      sub="«Nunca me avisó.»",
      son="Silencio de música 0.3 s en el corte (vacío) y vuelve el drone."),
 dict(id="c3", n="03", t="9.4 – 21.7 s", title="Clip 3 · «Nunca volvió a contactarme… que sí tomó la decisión»", frames=5,
      plano="Close-up frontal, 11.3 s con manos frente al pecho. Se parte en DOS envíos a Kling en la pausa natural (12.6 → 13.3 s: «Tiempo después») para no exceder la duración cómoda del motor; se unen en el mismo corte de palabra.",
      luz="Idéntica al clip 1 (misma referencia de luz, mismo still base). La linterna no se mueve: cualquier variación de luz entre tomas se ve como error.",
      motor="2 stills (o el mismo still) → 2× Kling MC → 2× Lipsync 2.0 (≈12 s de boca).",
      sub="«Nunca volvió a contactarme.» / «Tiempo después, buscó el mismo terreno,» / «pero ya no estaba disponible.» / «Estaba a nombre de alguien que sí tomó la decisión.»",
      son="Latido lento entra bajo la voz (a ≈60 bpm) y sube muy poco hasta el clip 7."),
 dict(id="c4", n="04", t="22.5 – 23.2 s", title="Clip 4 · «¿Y el terreno?» (perfil)", frames=7,
      plano="Close-up de lado, 2.5 s. Segundo cambio de ángulo: la pregunta retórica se hace en perfil mirando fuera de cuadro.",
      luz="Como clip 2.",
      motor="Still de perfil → Kling MC → Lipsync 2.0.",
      sub="«¿Y el terreno?»",
      son="Un golpe grave suave (sub) en «terreno»."),
 dict(id="c5", n="05", t="24.6 – 26.8 s", title="Clip 5 · «El terreno ya había duplicado su valor»", frames=8,
      plano="Frontal, 4.25 s. Aquí la cara puede acercarse un 10 % (push-in digital lento) para subir la tensión.",
      luz="Como clip 1.",
      motor="Mismo still base del clip 1 → Kling MC → Lipsync 2.0.",
      sub="«El terreno ya había duplicado su valor.» — «duplicado» un punto más grande.",
      son="Latido + cuerda disonante que crece."),
 dict(id="c6", n="06", t="27.0 – 28.4 s", title="Clip 6 · Detalle de la mano (pulgar, anillo, reloj)", frames=9,
      plano="Insert de 1.5 s: la mano con el pulgar, el anillo y el reloj café. Es el «te aviso» que nunca llegó.",
      luz="La linterna ilumina solo la mano; el resto negro.",
      motor="Tu mano REAL: no se hace swap (el reloj y el anillo ya son los del personaje). Solo keyer sobre negro + grading. 0 cr.",
      sub="Sin subtítulo.",
      son="Tic de reloj ×2, muy bajo."),
 dict(id="c7", n="07", t="28.4 – 31.4 s · apagón hasta 34.0 s", title="Clip 7 · «Lo que da miedo es dejar pasar oportunidades» → APAGÓN", frames=10,
      plano="Frontal, 3.5 s. Al terminar la frase, la linterna se APAGA de golpe (clic) y quedamos en negro 2.5 s. Es el momento cinematográfico central del video.",
      luz="Como clip 1 hasta el clic; después negro absoluto (ni grano, ni logo).",
      motor="Still base → Kling MC → Lipsync 2.0. El apagado se hace en edición (corte a negro en 2 cuadros + sonido).",
      sub="«LO QUE DA MIEDO» / «ES DEJAR PASAR OPORTUNIDADES» — la única frase en mayúsculas y más grande; se queda 1 s sobre el negro y se funde.",
      son="Clic de apagado · la música se corta en seco · 2.5 s de silencio con room tone."),
 dict(id="c8a", n="08a", t="34.1 – 37.5 s", title="Clip 8a · Se levanta del sillón y se hace la luz (showroom)", frames=12,
      plano="Plano medio (NO cuerpo entero): Felipe sentado en el sillón del showroom, se levanta hacia cámara. Las luces del showroom suben en 0.6 s desde negro.",
      luz="Transición de luz: de negro a la luz cálida real del showroom (fotos pro del showroom TR, ≈3200 K, cortinas con luz). Es el alivio del video: todo lo anterior era sombra.",
      motor="Still Nano Banana: Felipe sentado en el sillón sobre foto REAL del showroom TR (tenemos 11 fotos pro de Regina) → Kling MC con tu clip 8 (primera mitad) → Lipsync 2.0. Encendido de luces en edición (rampa de brillo + sonido).",
      sub="«En Terra Regia tenemos el terreno»",
      son="Clic de luces + zumbido suave de lámparas · la música cambia a pad cálido en mayor."),
 dict(id="c8b", n="08b", t="37.5 – 41.0 s", title="Clip 8b · CTA pecho-arriba «donde tu dinero sí crece. Conoce más en terraregia.com»", frames=13,
      plano="Pecho-arriba (cara ≥150 px), tono amable, media sonrisa. Decisión de David: la toma 8 se parte en dos para que Kling fije la identidad en el CTA.",
      luz="Luz del showroom, cálida, suave, frontal-lateral (ventana). Ya no hay linterna.",
      motor="Driver = tu clip 8 recortado al pecho (comp.py) → still pecho-arriba en el showroom → Kling MC → Lipsync 2.0.",
      sub="«donde tu dinero sí crece.» / «Conoce más en terraregia.com» — terraregia.com en verde TR.",
      son="Música cálida sube (sin ducking: envolvente fija como en Castelo)."),
 dict(id="outro", n="09", t="41.5 – 44.5 s", title="Outro · logo Terra Regia + terraregia.com", frames=None, outro=True,
      plano="Fondo NEGRO (no blanco: es terror), logo TR en blanco al centro, debajo «terraregia.com». 3 s.",
      luz="—",
      motor="Edición (PNG + ffmpeg). 0 cr.",
      sub="—",
      son="La música resuelve y se apaga en 0.8 s."),
]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;")
def img(src, alt): return f'<img src="{src}" alt="{esc(alt)}" loading="lazy">'

cards = []
for s in SC:
    if s.get("frames"): media = img(pair(s["frames"]), "izq: David en croma · der: referencia de Rudy") + '<div class="cap">izq. tu crudo en croma · der. referencia de Rudy (Genjutsu, descartada) — mismo instante</div>'
    elif s.get("intro"): media = '<div class="ph">Animación «¿Le temes a invertir?» — cerillo encendiéndose (ver Drive · 05_animacion_inicio)</div>'
    else: media = '<div class="ph outro"><span class="tr">TERRA REGIA</span><span class="url">terraregia.com</span></div>'
    test = ""
    if s.get("test"):
        test = f'''<div class="test"><h4>Prueba de identidad y lipsync (este clip)</h4>
        <div class="testgrid">
          <figure>{img(b64(f"{SB}/frames/cmp_identidad.jpg"), "ficha · David · ref luz · still A · still B")}<figcaption>ficha canónica · tu cuadro · referencia de luz · still A (luz plana, descartado) · <b>still B (elegido)</b></figcaption></figure>
          <figure><video controls playsinline preload="metadata" src="{'clip1_lipsync_540.mp4' if LIPSYNC else 'david_clip1_voz_jonas_540.mp4'}"></video><figcaption>{'Clip 1: still B + Kling Motion Control (tu actuación) + Lipsync 2.0 con la voz Jonas' if LIPSYNC else 'Tu clip 1 con la voz Jonas (el clip con Felipe se agrega al terminar Kling + Lipsync)'}</figcaption></figure>
        </div></div>'''
    cards.append(f'''
<section class="scene" id="{s["id"]}">
  <header><span class="n">{s["n"]}</span><div><h3>{esc(s["title"])}</h3><span class="tc">{s["t"]}</span></div></header>
  <div class="body">
    <div class="media">{media}</div>
    <dl>
      <div><dt>Plano y acción</dt><dd>{esc(s["plano"])}</dd></div>
      <div class="luz"><dt>Luz (bloque 11, manda)</dt><dd>{esc(s["luz"])}</dd></div>
      <div><dt>Motor y costo</dt><dd>{esc(s["motor"])}</dd></div>
      <div><dt>Subtítulo</dt><dd>{esc(s["sub"])}</dd></div>
      <div><dt>Sonido</dt><dd>{esc(s["son"])}</dd></div>
    </dl>
  </div>
  {test}
  <div class="approve" data-id="{s["id"]}">
    <div class="btns"><button class="ok">Aprobado</button><button class="chg">Cambiar</button><span class="st"></span></div>
    <textarea id="note-{s["id"]}" placeholder="Nota para este clip…"></textarea>
    <button class="save">Guardar nota</button>
  </div>
</section>''')

html = f'''<title>Miedo a invertir · Storyboard</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{{--ink:#0b0b0d;--panel:#141418;--line:#26262c;--bone:#e8e2d6;--mute:#9a948a;--amber:#f2b35b;--green:#2fa37a;--red:#c0493f;color-scheme:dark;
--serif:"Cormorant Garamond",Georgia,"Times New Roman",serif;--sans:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif;--mono:"IBM Plex Mono",Menlo,monospace}}
body{{background:var(--ink);color:var(--bone);font-family:var(--sans);font-size:15px;line-height:1.5;margin:0}}
.wrap{{max-width:1120px;margin:0 auto;padding-block:32px 80px;padding-inline:16px}}
h1{{font-family:var(--serif);font-weight:500;font-size:clamp(34px,6vw,58px);line-height:1;letter-spacing:-.01em;margin:0 0 8px;text-wrap:balance}}
h1 em{{font-style:italic;color:var(--amber)}}
.lead{{color:var(--mute);max-width:66ch;margin:0 0 6px}}
.meta{{font-family:var(--mono);font-size:12px;color:var(--mute);letter-spacing:.04em;text-transform:uppercase;display:flex;gap:18px;flex-wrap:wrap;margin:14px 0 36px}}
h2{{font-family:var(--serif);font-weight:500;font-size:28px;margin:48px 0 14px;letter-spacing:-.01em}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:16px 18px}}
.card h4{{margin:0 0 6px;font-size:14px;letter-spacing:.04em;text-transform:uppercase;color:var(--amber);font-weight:600}}
.card p,.card li{{margin:0;color:var(--bone)}} .card ul{{margin:6px 0 0;padding-left:18px}}
audio,video{{width:100%;max-width:100%;border-radius:4px;background:#000}}
figure{{margin:0}} figcaption,.cap{{font-size:12px;color:var(--mute);margin-top:6px}}
.scene{{border-top:1px solid var(--line);padding:26px 0 22px}}
.scene header{{display:flex;gap:16px;align-items:flex-start;margin-bottom:14px}}
.scene .n{{font-family:var(--mono);font-size:13px;color:var(--amber);border:1px solid var(--amber);border-radius:3px;padding:3px 7px;min-width:36px;text-align:center;margin-top:4px}}
.scene h3{{font-family:var(--serif);font-weight:600;font-size:24px;margin:0;line-height:1.15;text-wrap:balance}}
.tc{{font-family:var(--mono);font-size:12px;color:var(--mute)}}
.body{{display:grid;grid-template-columns:minmax(220px,300px) 1fr;gap:22px}}
@media (max-width:720px){{.body{{grid-template-columns:1fr}}}}
.media img{{width:100%;border-radius:4px;display:block}}
.ph{{aspect-ratio:9/16;max-height:420px;border:1px dashed var(--line);border-radius:4px;display:flex;align-items:center;justify-content:center;text-align:center;padding:18px;color:var(--mute);font-size:13px}}
.ph.outro{{background:#000;border-style:solid;flex-direction:column;gap:10px}} .tr{{font-family:var(--serif);font-size:28px;letter-spacing:.3em;color:#fff}} .url{{font-family:var(--mono);color:var(--green)}}
dl{{margin:0;display:grid;gap:10px}} dl>div{{display:grid;grid-template-columns:130px 1fr;gap:12px;align-items:start}}
@media (max-width:520px){{dl>div{{grid-template-columns:1fr}}}}
dt{{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);padding-top:3px}} dd{{margin:0}}
dl>div.luz dt{{color:var(--amber)}} dl>div.luz dd{{border-left:2px solid var(--amber);padding-left:10px}}
.test{{margin-top:18px;background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px 16px}}
.test h4{{margin:0 0 10px;font-size:13px;letter-spacing:.05em;text-transform:uppercase;color:var(--amber)}}
.testgrid{{display:grid;grid-template-columns:2fr 1fr;gap:14px;align-items:start}} @media (max-width:720px){{.testgrid{{grid-template-columns:1fr}}}}
.testgrid img{{width:100%;border-radius:4px}}
.approve{{margin-top:16px;display:grid;gap:8px}}
.btns{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}}
button{{font:inherit;font-size:13px;font-weight:600;border-radius:4px;border:1px solid var(--line);background:#1c1c22;color:var(--bone);padding:7px 14px;cursor:pointer}}
button:focus-visible{{outline:2px solid var(--amber);outline-offset:2px}}
button.ok{{border-color:var(--green);color:var(--green)}} button.ok.on{{background:var(--green);color:#06120d}}
button.chg{{border-color:var(--red);color:#e39a94}} button.chg.on{{background:var(--red);color:#fff}}
button.save{{justify-self:start}}
.st{{font-family:var(--mono);font-size:12px;color:var(--mute)}}
textarea{{font:inherit;font-size:14px;width:100%;min-height:64px;background:#101014;color:var(--bone);border:1px solid var(--line);border-radius:4px;padding:8px 10px;resize:vertical}}
.rule{{border-left:2px solid var(--amber);padding-left:12px;color:var(--bone)}}
.sum{{position:sticky;top:env(safe-area-inset-top,0px);background:rgba(11,11,13,.92);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:10px 0;margin:0 -16px 10px;padding-inline:16px;font-family:var(--mono);font-size:12px;color:var(--mute);z-index:2}}
.sum b{{color:var(--bone)}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>
<div class="wrap">
<div class="sum" id="sum">Aprobación: <b id="cnt">—</b> · las notas se guardan solas para Claude</div>
<h1>Miedo a invertir <em>· Episodio 1</em></h1>
<p class="lead">Storyboard para aprobar antes de la Versión 1. «El que nunca se decidió a invertir»: Felipe Juárez sobre tu actuación en croma, con la receta de Regina (still con la ficha → Kling Motion Control → Lipsync 2.0) y la ficha de toma de 14 bloques donde la luz manda.</p>
<div class="meta"><span>Terra Regia · Halloween 2026</span><span>Vertical 9:16 · 1080×1920 · ≈52 s</span><span>Voz: Jonas (ElevenLabs STS)</span><span>Avatar: Felipe Juárez 2.0</span></div>

<h2>Lo que vas a escuchar</h2>
<div class="grid2">
  <div class="card"><h4>Voz Jonas sobre tu toma completa (42 s)</h4><audio controls preload="metadata" src="voz_jonas_42s.mp3"></audio><p class="cap">Speech-to-speech: conserva tus tiempos, pausas y énfasis; cambia el timbre. Es la voz que mueve el lipsync.</p></div>
  <div class="card"><h4>Música de terror v1 (60 s, ElevenLabs Music)</h4><audio controls preload="metadata" src="musica_horror_v1.mp3"></audio><p class="cap">Drone grave + reloj + latido, cuerdas disonantes, se vacía antes del apagón y resuelve en un pad cálido al final. Sin ducking: cama fija y sube al terminar la voz (regla de Castelo).</p></div>
  <div class="card"><h4>Referencia de Rudy (la que vamos a superar)</h4><video controls playsinline preload="metadata" src="referencia_rudy_540.mp4"></video><p class="cap">Genjutsu 720p, voz incorrecta, sin intro ni outro, sin música. Sirve de guía de encuadres y luz.</p></div>
  <div class="card"><h4>Diseño de sonido</h4><ul>
    <li>Cerillo (intro) → clic de linterna ON (clip 1) → tic de reloj (clip 6) → clic OFF + silencio (clip 7) → luces del showroom (8a).</li>
    <li>Latido a 60 bpm bajo los clips 3–7, nunca por encima de la voz.</li>
    <li>Voz −21 dB · cama −27 dB · final −19 dB (medido como en Castelo).</li></ul></div>
</div>

<h2>Reglas cinematográficas que aplican a todo el video</h2>
<div class="grid2">
  <div class="card"><h4>Ficha de toma · 14 bloques (@andreaestratega)</h4><p>Cada still y cada prompt se escribe en este orden: contexto → referencias (la cara la pone la imagen) → mapa de locación y de dónde entra la luz → primer cuadro → formato → óptica/FOV → cámara → acción → actuación → física → <b>luz (manda: fuente, dirección, dureza, ratio, kelvin)</b> → grade → vestuario/audio → estilo/salida → <b>positive locks</b>.</p></div>
  <div class="card"><h4>Positive locks de este video</h4><ul><li>La linterna es la única luz y ya está encendida.</li><li>Reloj café en la muñeca izquierda (derecha de pantalla); anillo se queda.</li><li>La boca sigue la del actor; él es el único en cuadro; fondo negro puro.</li><li>Camisa verde #152A23 abierta sobre playera blanca.</li></ul></div>
  <div class="card"><h4>Aprendizajes de Regina que se heredan</h4><ul><li>Still con la ficha REAL, nunca copia de copia; cara ≥150 px o no hay identidad.</li><li>Kling encuadra según el driver: tu clip se recorta al encuadre del still.</li><li>Lipsync 2.0 sobre recorte 1:1 de la cara a 1280 px.</li><li>Música sin sidechain; subtítulos con tinta por palabra (claras sobre oscuro).</li></ul></div>
  <div class="card"><h4>Subtítulos (estilo cine, no real estate)</h4><p>Una línea por frase, serif (Cormorant/Didot), blanca, centrada en el tercio inferior, entra con la primera palabra y se va con la pausa. Solo la frase «LO QUE DA MIEDO…» va en mayúsculas y más grande. Sin colores, sin pop, sin acumulación por palabra.</p></div>
</div>

<h2>Presupuesto estimado</h2>
<div class="card"><p>Stills Nano Banana ≈ 10 × 75 = <b>750 cr Magnific</b> · Kling MC 1080p ≈ 10 × 15 = <b>150 cr Higgsfield</b> · Lipsync 2.0 ≈ 38 s de boca × 420 = <b>≈16,000 cr Magnific</b> (es el rubro grande; en Castelo fueron 3 tomas, aquí es todo el video a cuadro) · música 1,200 ya gastados · upscales y pruebas ≈ 2,000. <b>Total ≈ 20,000 cr Magnific + 150 Higgsfield.</b> Saldos hoy: Magnific 111,900 · Higgsfield 4,300.</p></div>

<h2>Escena por escena</h2>
{''.join(cards)}

<h2>Al aprobar</h2>
<p class="rule">Orden de producción: stills de identidad (frontal, perfil, sentado showroom, pecho showroom) → Kling MC por clip → Lipsync 2.0 → eventos de luz en edición (clic ON, apagón, luces) → intro/outro → montaje → música y SFX → subtítulos → QA con hoja de contacto de todas las frases.</p>
</div>
<script>
(async () => {{
  const ids = {json.dumps([s["id"] for s in SC])};
  const db = await claude.use("db");
  const cnt = document.getElementById("cnt");
  const state = {{}};
  function paint(id) {{
    const box = document.querySelector(`.approve[data-id="${{id}}"]`); const d = state[id] || {{}};
    box.querySelector(".ok").classList.toggle("on", d.status === "ok"); box.querySelector(".chg").classList.toggle("on", d.status === "chg");
    const ta = box.querySelector("textarea"); if (document.activeElement !== ta && typeof d.note === "string") ta.value = d.note;
    box.querySelector(".st").textContent = d.status === "ok" ? "aprobado" : d.status === "chg" ? "pide cambio" : "";
    const ok = ids.filter(i => (state[i]||{{}}).status === "ok").length, chg = ids.filter(i => (state[i]||{{}}).status === "chg").length;
    cnt.textContent = `${{ok}} aprobados · ${{chg}} con cambios · ${{ids.length - ok - chg}} pendientes`;
  }}
  ids.forEach(paint);
  if (!db) {{ cnt.textContent = "sin conexión a notas (solo lectura)"; return; }}
  db.collection("sb").onSnapshot(snap => {{ snap.docs.forEach(d => {{ state[d.id] = d.data(); }}); ids.forEach(paint); }}, e => {{ cnt.textContent = "notas no disponibles"; }});
  document.querySelectorAll(".approve").forEach(box => {{
    const id = box.dataset.id; const ref = db.doc("sb/" + id);
    const write = async (patch) => {{ const cur = state[id] || {{}}; const next = {{...cur, ...patch, at: new Date().toISOString()}}; state[id] = next; paint(id); try {{ await ref.set(next); }} catch (e) {{ box.querySelector(".st").textContent = "no se pudo guardar"; }} }};
    box.querySelector(".ok").addEventListener("click", () => write({{status: "ok"}}));
    box.querySelector(".chg").addEventListener("click", () => write({{status: "chg"}}));
    box.querySelector(".save").addEventListener("click", () => write({{note: box.querySelector("textarea").value}}));
  }});
}})();
</script>'''
os.makedirs(SB, exist_ok=True); open(f"{SB}/storyboard.html", "w").write(html); print("ok", f"{SB}/storyboard.html", round(len(html)/1e6, 2), "MB")
