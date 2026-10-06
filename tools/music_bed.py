#!/usr/bin/env python3
"""Cama de música con volumen PAREJO y envolvente fija (sin ducking). Pedido de David (DEMO 6 v2, 5-oct):
«debe empezar algo fuerte, luego disminuye un poco y se queda de acompañamiento todo el video; cuando Regina dice su
última línea subes el sonido hasta el final».
- Nivelación por RMS (ventana 1 s, numpy): la pista cruda varía ±8 dB sola (intro rala, drop fuerte, outro que se apaga) y
  dynaudnorm no lo corrige porque nivela picos, no energía.
- El tramo final (después de la última línea de Regina) se toma del DROP de la pista (segundo `drop`) con crossfade 0.5 s.
- Envolvente: `hi` 0–1.0 s → baja a `bed` en 1.0–2.4 s → `bed` constante → sube en 0.8 s al terminar T9 → `hi` → fade 0.8 s.
Uso: build(music_mp3, out_wav, total, t9_end, drop=20.0, hi=0.80, bed=0.30)
"""
import subprocess, numpy as np

SR = 48000

def _load(path, a, b):
    raw = subprocess.run(["ffmpeg","-v","error","-ss",f"{a:.3f}","-t",f"{b-a:.3f}","-i",path,"-f","f32le","-ac","2","-ar",str(SR),"-"],capture_output=True,check=True).stdout
    return np.frombuffer(raw, "float32").reshape(-1, 2).copy()

def level(x, win=1.0, target=0.12, gmin=0.4, gmax=4.0):
    """Gana por bloque para que el RMS (ventana `win`) sea `target`; la curva de ganancia se suaviza para no bombear."""
    n = int(SR*win); m = len(x)//n
    rms = np.sqrt((x[:m*n]**2).reshape(m, n, 2).mean(axis=(1, 2))) + 1e-6
    g = np.clip(target/rms, gmin, gmax)
    g = np.convolve(np.pad(g, 2, mode="edge"), np.ones(5)/5, mode="valid")  # suavizado 5 s
    t = np.arange(len(x))/n; gi = np.interp(t, np.arange(m)+0.5, g)
    return x*gi[:, None]

def build(music, out, total, t9_end, drop=20.0, hi=0.90, bed=0.36):
    a = level(_load(music, 0.0, t9_end+0.5))
    tail = total - t9_end + 1.0
    b = level(_load(music, drop, drop+tail))
    xf = int(SR*0.5); w = np.linspace(0, 1, xf)[:, None]
    head = a[:-xf]; mix = a[-xf:]*(1-w) + b[:xf]*w
    y = np.concatenate([head, mix, b[xf:]])[:int(SR*total)]
    t = np.arange(len(y))/SR
    env = np.where(t < 1.0, hi, np.where(t < 2.4, hi-(hi-bed)*(t-1.0)/1.4, np.where(t < t9_end, bed, np.where(t < t9_end+0.8, bed+(hi-bed)*(t-t9_end)/0.8, hi))))
    env *= np.clip(t/0.3, 0, 1) * np.clip((total-t)/0.8, 0, 1)  # fade in 0.3 s · fade out 0.8 s
    y = np.clip(y*env[:, None], -1, 1).astype("float32")
    subprocess.run(["ffmpeg","-v","error","-y","-f","f32le","-ac","2","-ar",str(SR),"-i","-","-c:a","pcm_s16le",out],input=y.tobytes(),check=True)
    return out

if __name__ == "__main__":
    import sys; build(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
