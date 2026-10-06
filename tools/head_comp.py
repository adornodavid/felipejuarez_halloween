#!/usr/bin/env python3
"""Compone una CABEZA animada (Kling MC sobre driver recortado, ya con lipsync) sobre el still aprobado completo:
cuerpo, manos y linterna quedan fijos (del still). Caída de luz radial opcional. Salida 1080x1920 30 fps.
Uso: head_comp.py still.png cabeza.mp4 salida.mp4 --place w,h,x,y --cut y0,y1 [--audio voz.wav] [--feather 60] [--light cx,cy,r0,r1,floor]
  --place : tamaño y posición (px del STILL) en que se coloca el video de cabeza escalado (alinear ojos y barbilla con el still).
  --cut   : rampa inferior de la máscara en px del STILL (1 arriba de y0, 0 debajo de y1), sobre la barbilla/barba.
  --light : centro de la linterna (px del still), radio sin caída r0, radio de caída total r1, nivel mínimo floor (0-1).
"""
import sys, subprocess, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
a = sys.argv; still, head, out = a[1:4]
def opt(k, d=None): return a[a.index(k)+1] if k in a else d
pw,ph,px,py = map(int, opt("--place").split(",")); cy0,cy1 = map(int, opt("--cut").split(","))
audio = opt("--audio"); feather = int(opt("--feather", 60)); light = opt("--light")
OW, OH, FPS = 1080, 1920, 30
S = np.asarray(Image.open(still).convert("RGB")).astype(np.float32); H, W, _ = S.shape
# región de pegado recortada al lienzo
X0,Y0 = max(px,0), max(py,0); X1,Y1 = min(px+pw,W), min(py+ph,H)
m = np.ones((ph, pw), np.float32); ramp = lambda n: np.linspace(0,1,n,dtype=np.float32)
m[:, :feather] *= ramp(feather)[None,:]; m[:, -feather:] *= ramp(feather)[::-1][None,:]; m[:feather,:] *= ramp(feather)[:,None]
yy = np.arange(ph)[:,None] + py; m *= np.clip((cy1 - yy)/(cy1-cy0), 0, 1)
m = m[Y0-py:Y1-py, X0-px:X1-px, None]
L = None
if light:
    cx,cy,r0,r1,floor = map(float, light.split(",")); gy,gx = np.mgrid[:H,:W]; d = np.sqrt((gx-cx)**2+(gy-cy)**2)
    t = np.clip((d-r0)/(r1-r0),0,1); L = (1-(1-floor)*(t*t*(3-2*t)))[...,None].astype(np.float32)
pr = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",head],capture_output=True,text=True).stdout.strip().split(",")
hw,hh = int(pr[0]),int(pr[1])
dec = subprocess.Popen(["ffmpeg","-v","error","-i",head,"-vf",f"fps={FPS}","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
cmd = ["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{OW}x{OH}","-r",str(FPS),"-i","-"]
if audio: cmd += ["-i",audio,"-map","0:v","-map","1:a","-c:a","aac","-b:a","192k","-shortest"]
cmd += ["-c:v","libx264","-crf","12","-pix_fmt","yuv420p",out]
enc = subprocess.Popen(cmd, stdin=subprocess.PIPE); n = 0
while True:
    b = dec.stdout.read(hw*hh*3)
    if len(b) < hw*hh*3: break
    f = np.asarray(Image.fromarray(np.frombuffer(b,np.uint8).reshape(hh,hw,3)).resize((pw,ph),Image.LANCZOS),np.float32)[Y0-py:Y1-py, X0-px:X1-px]
    o = S.copy(); o[Y0:Y1,X0:X1] = f*m + o[Y0:Y1,X0:X1]*(1-m)
    if L is not None: o *= L
    enc.stdin.write(np.asarray(Image.fromarray(o.clip(0,255).astype(np.uint8)).resize((OW,OH),Image.LANCZOS)).tobytes()); n += 1
enc.stdin.close(); enc.wait(); print("ok", out, n, "cuadros")
