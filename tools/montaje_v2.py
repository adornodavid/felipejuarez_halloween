#!/usr/bin/env python3
"""Montaje DEMO 2 (6-oct) — correcciones de David sobre la V1:
  intro cerillo 6 s → c1 CON ENCENDIDO (negro → clic → luz) → c2 c3a c3b c4 c5 c6(mano) c7_v2 → APAGÓN 2.5 s →
  c8a2 (sentado, deja la linterna en la mesa real; luces suben 0.6 s) → c8b2 (de pie, plano medio, CTA) → outro logo TR 3 s.
Escribe build/v2/timeline.json con el offset de cada clip (nuevo_inicio − inicio_en_el_crudo) para los subtítulos.
Uso: montaje_v2.py [intro.mp4]
"""
import subprocess, json, os, sys
from PIL import Image, ImageDraw, ImageFont
W, H, FPS = 1080, 1920, 30; OUT = "build/v2"; os.makedirs(OUT, exist_ok=True)
def dur(p): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())
def run(c): subprocess.run(c, check=True)
INTRO = sys.argv[1] if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else None
INTRO_LEN = 6.0
# (nombre, archivo, inicio en el crudo de David del PRIMER cuadro del clip, fade-in s)
CLIPS = [("c1", "build/clips/c1_felipe_encendido.mp4", -0.06, 0),
         ("c2", "build/clips/c2_felipe.mp4", 6.54, 0), ("c3a", "build/clips/c3a_felipe.mp4", 8.46, 0),
         ("c3b", "build/clips/c3b_felipe.mp4", 13.0, 0), ("c4", "build/clips/c4_felipe.mp4", 19.79, 0),
         ("c5", "build/clips/c5_felipe.mp4", 22.29, 0), ("c6", "build/clips/c6_mano_mudo.mp4", 26.54, 0),
         ("c7", "build/clips/c7_felipe_v2.mp4", 28.08, 0),
         ("APAGON", None, None, 0),
         ("c8a", "build/clips/c8a2_felipe.mp4", 32.58, 0.6), ("c8b", "build/clips/c8b2_felipe.mp4", 34.0, 0)]
ROOM = "anoisesrc=color=pink:amplitude=0.0025:r=48000,aformat=channel_layouts=stereo"
def black(sec, name):
    p = f"{OUT}/{name}.mp4"; run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={sec}", "-f", "lavfi", "-i", ROOM, "-t", str(sec), "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", p]); return p
def norm(src, name, fade=0, trim=None, afade_out=None):
    p = f"{OUT}/{name}.mp4"; d = dur(src) if trim is None else min(trim, dur(src))
    has_a = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=codec_type", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip() != ""
    vf = f"scale={W}:-2:flags=lanczos,crop={W}:{H},fps={FPS},format=yuv420p" + (f",fade=t=in:st=0:d={fade}" if fade else "")
    cmd = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src]
    if not has_a: cmd += ["-f", "lavfi", "-i", ROOM]
    af = "aformat=sample_rates=48000:channel_layouts=stereo" + (f",afade=t=out:st={d-afade_out}:d={afade_out}" if afade_out else "")
    cmd += ["-filter:v", vf, "-filter:a", af, "-map", "0:v", "-map", ("1:a" if not has_a else "0:a"), "-t", f"{d:.3f}", "-c:v", "libx264", "-crf", "14", "-c:a", "aac", "-b:a", "192k", p]
    run(cmd); return p
def outro(sec=3.0):
    logo = Image.open(os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/logos/TR_white.png")).convert("RGBA")
    lw = 560; logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255)); im.alpha_composite(logo, ((W - lw) // 2, H // 2 - logo.height - 30))
    f = ImageFont.truetype(os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/fonts/HELVETICANOWDISPLAY-MEDIUM.TTF"), 46)
    d = ImageDraw.Draw(im); t = "terraregia.com"; bb = d.textbbox((0, 0), t, font=f); d.text(((W - (bb[2] - bb[0])) // 2, H // 2 + 50), t, font=f, fill=(255, 255, 255, 235))
    im.convert("RGB").save(f"{OUT}/outro.png")
    p = f"{OUT}/outro.mp4"; run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-i", f"{OUT}/outro.png", "-f", "lavfi", "-i", ROOM, "-t", str(sec), "-vf", f"fps={FPS},format=yuv420p,fade=t=in:st=0:d=0.5,fade=t=out:st={sec-0.6}:d=0.6", "-c:v", "libx264", "-crf", "14", "-c:a", "aac", "-b:a", "192k", "-shortest", p]); return p
parts = []; tl = []; t = 0.0
if INTRO:
    p = norm(INTRO, "intro", trim=INTRO_LEN, afade_out=0.6)
    parts.append(p); tl.append(dict(name="intro", start=t, dur=dur(p))); t += dur(p)
for name, src, orig, fade in CLIPS:
    if name == "APAGON": p = black(2.5, "apagon"); d = 2.5; orig = 31.58
    else: p = norm(src, f"n_{name}", fade); d = dur(p)
    parts.append(p); tl.append(dict(name=name, start=round(t, 3), dur=round(d, 3), orig=orig, offset=round(t - orig, 3))); t += d
p = outro(); parts.append(p); tl.append(dict(name="outro", start=t, dur=3.0)); t += 3.0
with open(f"{OUT}/concat.txt", "w") as f:
    for p in parts: f.write(f"file '{os.path.abspath(p)}'\n")
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{OUT}/concat.txt", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{OUT}/v2_cuerpo_sin_musica.mp4"])
json.dump(dict(total=round(t, 3), parts=tl), open(f"{OUT}/timeline.json", "w"), indent=1, ensure_ascii=False)
print("total", round(t, 2), "s")
for x in tl: print(f"  {x['name']:<7} {x['start']:>6.2f} +{x['dur']:.2f}" + (f"  offset {x['offset']:+.2f}" if x.get('offset') is not None else ""))
