#!/usr/bin/env python3
"""Subtítulos v2 (ref. @homeflexmedia) como módulo reutilizable. Aprobado en el test del DEMO 5 (5-oct-2026).
- Frase = bloque; cada palabra entra en su `start` de ElevenLabs scribe y se queda hasta el fin de la frase.
- 3 niveles: CON (Helvetica Now Medium 58, blanco 88 %) · MOD (Didot Italic 80) · KEY (Helvetica Now Bold MAYÚSCULAS 156, acento TR con degradado).
- KEY: revelado por máscara izq→der en 5 cuadros con blur decreciente y subida de 14 px · CON/MOD: suben 18 px y se asientan en 3 cuadros.
- Contraste automático: luminancia media del fondo detrás del bloque en el cuadro de arranque de la frase; >150 ⇒ tinta oscura #1F2D3B.
Uso: apply(video_in, video_out, toma, spec, offset=0.0, end=None, y0=880, tag="t1")
  spec = lista de frases; frase = dict(lines=[[(texto, rol, n_palabras=1), ...], ...], color=(hex1, hex2) opcional).
  Cada token consume `n` palabras del scribe en orden (p. ej. ("169","KEY",4) = «ciento sesenta y nueve»).
  offset/end recortan a la parte de la toma que vive en ese bloque (la toma partida en dos bloques).
"""
import os, json, subprocess, io, unicodedata
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTS = os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/fonts")
HB, HM = f"{FONTS}/HELVETICANOWDISPLAY-BOLD.TTF", f"{FONTS}/HELVETICANOWDISPLAY-MEDIUM.TTF"
DIDOT = "/System/Library/Fonts/Supplemental/Didot.ttc"  # index 1 = Italic
W, H, FPS = 1080, 1920, 30
SZ = {"CON": 58, "MOD": 80, "KEY": 156}; MAXW = 860
ACCENTS = [("#1A815D", "#5CCB8F"), ("#005E69", "#3FB8C4"), ("#E6D3AE", "#E6D3AE")]  # verde · teal · arena (Castelo)
B = "build/subsv2"

def _run(c): subprocess.run(c, check=True)
def _dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())
def _norm(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn").strip(".,:;¿?¡!")
def font(role, size): return ImageFont.truetype(DIDOT, size, index=1) if role == "MOD" else ImageFont.truetype(HB if role == "KEY" else HM, size)
def hexrgb(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def words(toma):
    return [(w["text"], w["start"], w["end"]) for w in json.load(open(f"build/words/{toma}.json"))["words"] if w.get("type") == "word"]

def timed(toma, spec):
    """Asigna a cada token el start de su primera palabra. Verifica que el spec consuma TODAS las palabras en orden."""
    ws = words(toma); i = 0; out = []
    for ph in spec:
        lines = []
        for line in ph["lines"]:
            row = []
            for tok in line:
                txt, role, n = (tok + (1,))[:3]
                if i + n > len(ws): raise SystemExit(f"{toma}: el spec pide más palabras de las que hay ({txt})")
                if n == 1 and _norm(txt) != _norm(ws[i][0]): print(f"  ⚠️ {toma}: «{txt}» ≠ scribe «{ws[i][0]}»")
                row.append((txt, role, ws[i][1], ws[i+n-1][2])); i += n
            lines.append(row)
        out.append(dict(ph, lines=lines))
    if i != len(ws): raise SystemExit(f"{toma}: sobran {len(ws)-i} palabras sin subtítulo: {[w[0] for w in ws[i:]]}")
    return out

def layout(ph):
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10))); items = []; y = 0; bw = 0
    for line in ph["lines"]:
        k = SZ["KEY"]
        while True:
            x = 0; lh = 0; row = []
            for txt, r, a, b in line:
                s = k if r == "KEY" else SZ[r]; t = txt.upper() if r == "KEY" else txt
                bb = tmp.textbbox((0, 0), t, font=font(r, s)); w_, h_ = bb[2]-bb[0], bb[3]-bb[1]
                row.append((t, r, x, s, w_, h_, a)); x += w_ + int(s*0.28); lh = max(lh, h_)
            lw = x - int(row[-1][3]*0.28)
            if lw <= MAXW or k <= 72: break
            k -= 6
        for t, r, x, s, w_, h_, a in row: items.append((t, r, x, y+(lh-h_), s, w_, h_, a, lw))
        bw = max(bw, lw); y += lh + 14
    return items, bw, y

def word_png(path, txt, role, size, color=None, reveal=None, blur=0, scale=1.0, dark=False):
    f = font(role, int(size*scale)); tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10))); bb = tmp.textbbox((0, 0), txt, font=f)
    w_, h_ = bb[2]-bb[0]+40, bb[3]-bb[1]+40
    shcol = (255, 255, 255, 120) if dark else (0, 0, 0, 170)
    sh = Image.new("RGBA", (w_, h_), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((20-bb[0]+4, 20-bb[1]+6), txt, font=f, fill=shcol); sh = sh.filter(ImageFilter.GaussianBlur(9))
    if role == "KEY" and color:
        c1, c2 = np.array(hexrgb(color[0]), "float32"), np.array(hexrgb(color[1]), "float32")
        t = np.linspace(0, 1, w_, dtype="float32")[None, :, None]
        grad = (c1 + (c2-c1)*t).repeat(h_, 0).astype("uint8")
        mask = Image.new("L", (w_, h_), 0); ImageDraw.Draw(mask).text((20-bb[0], 20-bb[1]), txt, font=f, fill=255)
        txtim = Image.new("RGBA", (w_, h_), (0, 0, 0, 0)); txtim.paste(Image.fromarray(grad, "RGB").convert("RGBA"), (0, 0), mask)
    else:
        a = 255 if role != "CON" else 225; ink = (31, 45, 59, a) if dark else (255, 255, 255, a)
        txtim = Image.new("RGBA", (w_, h_), (0, 0, 0, 0)); ImageDraw.Draw(txtim).text((20-bb[0], 20-bb[1]), txt, font=f, fill=ink)
    out = Image.alpha_composite(sh, txtim)
    if reveal is not None and reveal < 1:
        m = Image.new("L", (w_, h_), 0); ImageDraw.Draw(m).rectangle((0, 0, int(w_*reveal), h_), fill=255); m = m.filter(ImageFilter.GaussianBlur(12))
        out.putalpha(Image.fromarray((np.asarray(out.split()[3]).astype("float32")*np.asarray(m).astype("float32")/255).astype("uint8")))
    if blur: out = out.filter(ImageFilter.GaussianBlur(blur))
    out.save(path); return path, w_, h_

def overlays(video, toma, spec, offset=0.0, end=None, y0=880, tag="t", ci=0, ink=None):
    """ink: None = automático por luminancia · "light" = letras claras · "dark" = letras oscuras (override por bloque)."""
    """Devuelve [(png, x, y, a, b)] en el tiempo del bloque (t_bloque = t_toma - offset)."""
    os.makedirs(B, exist_ok=True); L = _dur(video); end = L if end is None else end; out = []
    phs = [p for p in timed(toma, spec) if offset - 0.01 <= p["lines"][0][0][2] < offset + L]
    for pi, ph in enumerate(phs):
        items, bw, bh = layout(ph)
        a0 = ph["lines"][0][0][2] - offset; last = ph["lines"][-1][-1][3] - offset
        fin = last + 0.35
        if pi+1 < len(phs): fin = min(fin, phs[pi+1]["lines"][0][0][2] - offset - 0.02)
        fin = min(fin, L)
        x0 = (W - bw)//2
        fr = subprocess.run(["ffmpeg","-v","error","-ss",f"{max(a0+0.15,0):.2f}","-i",video,"-frames:v","1","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
        # contraste: se mide la FRANJA CENTRAL del bloque (donde caen las palabras), no todo el ancho; percentil 70 para que
        # una prenda clara en medio (top beige de Regina) mande aunque los lados sean oscuros (blazer).
        reg = Image.open(io.BytesIO(fr)).convert("L").resize((W, H)).crop((max(x0+int(bw*0.2), 0), y0, min(x0+int(bw*0.8), W), min(y0+bh, H)))
        lum = float(np.percentile(np.asarray(reg), 70)); dark = (lum > 140) if ink is None else (ink == "dark")
        color = ph.get("color") or ACCENTS[(ci+pi) % len(ACCENTS)]
        if dark: color = ("#005E69", "#1A815D")
        print(f"  {tag} frase {pi}: lum {lum:.0f} ⇒ {'OSCURA' if dark else 'blanca'} · {' / '.join(' '.join(t for t,*_ in l) for l in ph['lines'])}", flush=True)
        # centrar cada renglón dentro del bloque
        for k, (txt, r, rx, ry, s, w_, h_, a, lw) in enumerate(items):
            a -= offset; x = x0 + (bw-lw)//2 + rx - 20; y = y0 + ry - 20; base = f"{B}/{tag}_{pi}_{k}"
            if r == "KEY":
                for j in range(5):
                    p, _, _ = word_png(f"{base}_r{j}.png", txt, r, s, color, reveal=(j+1)/5, blur=(4-j)*2.5, dark=dark)
                    out.append((p, x, y+int(14*(4-j)/4), a+j/FPS, a+(j+1)/FPS))
                p, _, _ = word_png(f"{base}.png", txt, r, s, color, dark=dark); out.append((p, x, y, a+5/FPS, fin))
            else:
                p1, w1, h1 = word_png(f"{base}_p1.png", txt, r, s, scale=1.10, dark=dark, blur=1.5); out.append((p1, x-(w1-w_-40)//2, y-(h1-h_-40)//2+18, a, a+1/FPS))
                p2, w2, h2 = word_png(f"{base}_p2.png", txt, r, s, scale=1.04, dark=dark); out.append((p2, x-(w2-w_-40)//2, y-(h2-h_-40)//2+8, a+1/FPS, a+2/FPS))
                p, _, _ = word_png(f"{base}.png", txt, r, s, dark=dark); out.append((p, x, y, a+2/FPS, fin))
    return out

def apply(video_in, video_out, toma, spec, offset=0.0, y0=880, tag="t", ci=0, ink=None):
    """Quema los subtítulos v2 sobre un bloque ya montado (video+audio). Copia el audio sin tocar."""
    ov = overlays(video_in, toma, spec, offset=offset, y0=y0, tag=tag, ci=ci, ink=ink)
    fc = "[0:v]null[base]"; cur = "base"; inputs = []
    for i, (p, x, y, a, b) in enumerate(ov):
        inputs += ["-loop", "1", "-i", os.path.abspath(p)]
        fc += f";[{cur}][{i+1}:v]overlay={int(x)}:{int(y)}:enable='between(t,{a:.3f},{b:.3f})':format=auto[v{i}]"; cur = f"v{i}"
    fc += f";[{cur}]format=yuv420p[v]"
    _run(["ffmpeg","-v","error","-y","-i",video_in]+inputs+["-filter_complex",fc,"-map","[v]","-map","0:a","-t",f"{_dur(video_in):.3f}",
          "-c:v","libx264","-crf","16","-r",str(FPS),"-c:a","copy",video_out])
    return video_out
