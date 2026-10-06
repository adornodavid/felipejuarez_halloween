#!/usr/bin/env python3
"""Zoom dinámico (push-in) con trayectoria por keyframes: zoom_path.py in.mp4 out.mp4 "t,cx,cy,zoom;t,cx,cy,zoom;..."
cx,cy en px del video de ENTRADA (centro de la ventana), zoom = factor (1 = cuadro completo). Interpola suave (smoothstep) entre keyframes.
Salida 1080x1920 30 fps, sin audio."""
import sys, subprocess, numpy as np
from PIL import Image
src,out,kf=sys.argv[1:4]; OW,OH,FPS=1080,1920,30
keys=[tuple(map(float,k.split(","))) for k in kf.split(";")]
pr=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",src],capture_output=True,text=True).stdout.strip().split(","); W,H=int(pr[0]),int(pr[1])
def interp(t):
    if t<=keys[0][0]: return keys[0][1:]
    for a,b in zip(keys,keys[1:]):
        if a[0]<=t<=b[0]:
            u=(t-a[0])/(b[0]-a[0]) if b[0]>a[0] else 1; s=u*u*(3-2*u)
            return tuple(a[i]+(b[i]-a[i])*s for i in (1,2,3))
    return keys[-1][1:]
dec=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-vf",f"fps={FPS}","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
enc=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{OW}x{OH}","-r",str(FPS),"-i","-","-c:v","libx264","-crf","12","-pix_fmt","yuv420p",out],stdin=subprocess.PIPE)
n=0
while True:
    b=dec.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    cx,cy,z=interp(n/FPS); ch=H/z; cw=ch*OW/OH
    if cw>W: cw=W; ch=cw*OH/OW
    x0=min(max(cx-cw/2,0),W-cw); y0=min(max(cy-ch/2,0),H-ch)
    im=Image.fromarray(np.frombuffer(b,np.uint8).reshape(H,W,3)).crop((x0,y0,x0+cw,y0+ch)).resize((OW,OH),Image.LANCZOS)
    enc.stdin.write(np.asarray(im).tobytes()); n+=1
enc.stdin.close(); enc.wait(); print("ok",out,n,"cuadros")
