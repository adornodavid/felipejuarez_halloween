#!/usr/bin/env python3
"""Subtítulos de CINE v2 (DEMO 2): igual que subs_cine.py (Minion Pro, una línea, palabra que suena en ámbar) +
TÍTULO GRANDE «terraregia.com» que se completa con el gesto de manos de Felipe al final (barrido izq→der con borde suave,
desde que arranca la palabra hasta el pico del gesto; se queda hasta el fin del clip). La frase 15 queda «Conoce más en».
Uso: python tools/subs_cine_v2.py in.mp4 out.mp4 [timeline.json=build/v2/timeline.json] [y0=1430]
"""
import json, os, subprocess, sys, io, unicodedata
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1080, 1920, 30; MAXW = 920; SIZE = 58; AMBER = (242, 193, 78); WHITE = (255, 255, 255); DARK = (31, 45, 59)
FONTS = os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/fonts")
FONT = f"{FONTS}/MinionPro-Regular.otf"; BIGFONT = f"{FONTS}/HELVETICANOWDISPLAY-BOLD.TTF"
B = "build/subscine2"; os.makedirs(B, exist_ok=True)
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn").strip('.,:;¿?¡!"«»')
PHRASES = ["Vio el terreno, le gustó.", "Dijo: «Lo pienso, te aviso».", "Nunca me avisó.", "Nunca volvió a contactarme.", "Tiempo después,",
           "buscó el mismo terreno,", "pero ya no estaba disponible.", "Estaba a nombre de alguien", "que sí tomó la decisión.", "¿Y el terreno?",
           "El terreno ya había duplicado su valor.", "Lo que da miedo", "es dejar pasar oportunidades.", "En Terra Regia tenemos el terreno",
           "donde tu dinero sí crece.", "Conoce más en"]
BIG = "terraregia.com"; BIG_SIZE = 104; BIG_Y = 1250; GESTURE_PEAK_ORIG = 41.8   # pico del gesto de brazos abiertos en el crudo
words = [w for w in json.load(open("media/04_referencia_resultado/david_words.json"))["words"] if w["type"] == "word"]
src, out = sys.argv[1], sys.argv[2]
TLP = sys.argv[3] if len(sys.argv) > 3 else "build/v2/timeline.json"; y0 = int(sys.argv[4]) if len(sys.argv) > 4 else 1430
tl = json.load(open(TLP))["parts"]
def newtime(t):
    for p in tl:
        if p["name"] != "APAGON" and p.get("orig") is not None and p["orig"] - 0.05 <= t < p["orig"] + p["dur"] + 0.05: return t + p["offset"]
    return None
f = ImageFont.truetype(FONT, SIZE); tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
def wbox(t, fnt=f): bb = tmp.textbbox((0, 0), t, font=fnt); return bb[2] - bb[0], bb[3] - bb[1], bb
i = 0; phrases = []
for ph in PHRASES:
    row = []
    for tok in ph.split():
        if norm(tok) != norm(words[i]["text"]): print(f"⚠️ «{tok}» ≠ scribe «{words[i]['text']}»")
        row.append((tok, words[i]["start"], words[i]["end"])); i += 1
    phrases.append(row)
bigword = words[i]; i += 1
if i != len(words): print("⚠️ sobran palabras:", [w["text"] for w in words[i:]])
L = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout)
ov = []
for pi, row in enumerate(phrases):
    a = newtime(row[0][1]); b = newtime(row[-1][2])
    if a is None or b is None: print("⚠️ frase fuera de timeline:", row); continue
    fin = b + 0.45
    if pi + 1 < len(phrases):
        na = newtime(phrases[pi + 1][0][1])
        if na: fin = min(fin, na - 0.04)
    if pi == len(phrases) - 1: fin = min(fin, newtime(bigword["start"]) + 1.6)   # «Conoce más en» se va cuando el título ya entró
    sp = int(SIZE * 0.27); xs = []; x = 0
    for tok, _, _ in row: w_, h_, _ = wbox(tok); xs.append((x, w_)); x += w_ + sp
    lw = x - sp; x0 = (W - lw) // 2
    if lw > MAXW: print(f"⚠️ frase {pi} ancha: {lw}px")
    fr = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{a+0.1:.2f}", "-i", src, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    reg = Image.open(io.BytesIO(fr)).convert("L").crop((max(x0, 0), y0 - 10, min(x0 + lw, W), y0 + SIZE + 20)); lum = float(np.percentile(np.asarray(reg), 70)); dark = lum > 140
    base = DARK if dark else WHITE
    print(f"frase {pi:>2} {a:6.2f}–{fin:6.2f} lum {lum:3.0f} {'OSCURA' if dark else 'blanca'}  {' '.join(t for t,_,_ in row)}")
    states = [(k, newtime(ws)) for k, (tok, ws, we) in enumerate(row)] + [(len(row), fin)]
    for k in range(len(row)):
        im = Image.new("RGBA", (W, SIZE + 80), (0, 0, 0, 0)); sh = Image.new("RGBA", (W, SIZE + 80), (0, 0, 0, 0)); dsh = ImageDraw.Draw(sh)
        for j, (tok, _, _) in enumerate(row): dsh.text((x0 + xs[j][0] + 3, 45), tok, font=f, fill=(255, 255, 255, 110) if dark else (0, 0, 0, 190))
        sh = sh.filter(ImageFilter.GaussianBlur(8)); d = ImageDraw.Draw(im)
        for j, (tok, _, _) in enumerate(row): d.text((x0 + xs[j][0], 40), tok, font=f, fill=(AMBER if j == k else base) + (255 if j <= k else 215,))
        png = f"{B}/p{pi}_{k}.png"; Image.alpha_composite(sh, im).save(png)
        t0 = a if k == 0 else max(states[k][1], a); t1 = states[k + 1][1]
        ov.append((png, 0, y0 - 40, t0, max(t1, t0 + 1 / FPS)))
# ---- título grande terraregia.com: barrido izq→der entre el inicio de la palabra y el pico del gesto; se queda hasta el fin del clip c8b
bf = ImageFont.truetype(BIGFONT, BIG_SIZE); bw, bh, bb = wbox(BIG, bf); bx = (W - bw) // 2
t_start = newtime(bigword["start"]); t_peak = newtime(GESTURE_PEAK_ORIG) or (t_start + 1.6)
c8b = [p for p in tl if p["name"] == "c8b"][0]; t_end = c8b["start"] + c8b["dur"]
# contraste del título
fr = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t_start+0.3:.2f}", "-i", src, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
lumb = float(np.percentile(np.asarray(Image.open(io.BytesIO(fr)).convert("L").crop((bx, BIG_Y, bx + bw, BIG_Y + bh))), 70)); darkb = lumb > 150
ink = (31, 45, 59, 255) if darkb else (255, 255, 255, 255); shcol = (255, 255, 255, 120) if darkb else (0, 0, 0, 200)
print(f"título {BIG} {t_start:.2f}→{t_peak:.2f} hold→{t_end:.2f} lum {lumb:.0f} {'OSCURO' if darkb else 'blanco'}")
STEPS = 24; pad = 60
base = Image.new("RGBA", (bw + 2 * pad, bh + 2 * pad), (0, 0, 0, 0))
sh = Image.new("RGBA", base.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).text((pad - bb[0] + 4, pad - bb[1] + 8), BIG, font=bf, fill=shcol); sh = sh.filter(ImageFilter.GaussianBlur(14))
txt = Image.new("RGBA", base.size, (0, 0, 0, 0)); ImageDraw.Draw(txt).text((pad - bb[0], pad - bb[1]), BIG, font=bf, fill=ink)
full = Image.alpha_composite(sh, txt)
for s in range(1, STEPS + 1):
    r = s / STEPS; m = Image.new("L", base.size, 0); ImageDraw.Draw(m).rectangle((0, 0, int(base.size[0] * r), base.size[1]), fill=255); m = m.filter(ImageFilter.GaussianBlur(18))
    im = full.copy(); im.putalpha(Image.fromarray((np.asarray(full.split()[3]).astype("float32") * np.asarray(m).astype("float32") / 255).astype("uint8")))
    p = f"{B}/big_{s:02d}.png"; im.save(p)
    ta = t_start + (t_peak - t_start) * (s - 1) / STEPS; tb = t_start + (t_peak - t_start) * s / STEPS if s < STEPS else t_end
    ov.append((p, bx - pad, BIG_Y - pad, ta, tb))
# ---- render rápido: composición numpy cuadro a cuadro (el grafo de ffmpeg con ~100 overlays tardaba >10 min)
pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split(",")
SW, SH = int(pr[0]), int(pr[1])
cache = {}
def load(p):
    if p not in cache:
        im = np.asarray(Image.open(p).convert("RGBA")).astype(np.float32); cache[p] = (im[..., :3], im[..., 3:4] / 255.0)
    return cache[p]
ov.sort(key=lambda o: o[3])
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{SW}x{SH}", "-r", str(FPS), "-i", "-", "-i", src, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "15", "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", out], stdin=subprocess.PIPE)
n = 0
while True:
    buf = dec.stdout.read(SW * SH * 3)
    if len(buf) < SW * SH * 3: break
    t = n / FPS; act = [o for o in ov if o[3] <= t < o[4]]
    if act:
        fr = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3).astype(np.float32)
        for p, x, y, a, b in act:
            rgb, al = load(p); h, w = al.shape[:2]; x, y = int(x), int(y)
            x0, y0 = max(x, 0), max(y, 0); x1, y1 = min(x + w, SW), min(y + h, SH)
            if x1 <= x0 or y1 <= y0: continue
            sub = fr[y0:y1, x0:x1]; A = al[y0 - y:y1 - y, x0 - x:x1 - x]; C = rgb[y0 - y:y1 - y, x0 - x:x1 - x]
            fr[y0:y1, x0:x1] = C * A + sub * (1 - A)
        enc.stdin.write(fr.clip(0, 255).astype(np.uint8).tobytes())
    else:
        enc.stdin.write(buf)
    n += 1
enc.stdin.close(); enc.wait()
print("ok", out, len(ov), "overlays", n, "cuadros")
