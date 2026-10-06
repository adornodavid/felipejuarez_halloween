#!/usr/bin/env python3
"""Lipsync en recorte de cara (más píxeles para la boca) y recomposición.

  python tools/facecrop.py crop  clip.mp4 salida_crop.mp4 cx,cy,size [--out 1280]
      Recorta un cuadro 1:1 centrado en (cx,cy) px de lado `size` y lo escala a --out px (default 1280).
  python tools/facecrop.py paste clip.mp4 crop_lipsync.mp4 salida.mp4 cx,cy,size [--feather 40]
      Pega el recorte procesado de vuelta en el clip original, con borde difuminado (máscara radial/cuadrada suave).

El recorte se hace con pares (cx,cy) y lado en píxeles del clip ORIGINAL. El clip de vuelta conserva la resolución,
fps y duración del original (si el lipsync cambió fps/duración, se re-muestrea al original).
"""
import sys, subprocess, os

def probe(p):
    out = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout.strip().split("\n")
    w,h,fr = out[0].split(",")[:3]; dur = float(out[1]) if len(out)>1 and out[1] else None
    return int(w), int(h), fr, dur

def crop(src, out, cx, cy, size, outpx=1280):
    w,h,fr,_ = probe(src); x0 = max(0, min(w-size, cx-size//2)); y0 = max(0, min(h-size, cy-size//2))
    subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-vf",f"crop={size}:{size}:{x0}:{y0},scale={outpx}:{outpx}:flags=lanczos","-c:v","libx264","-crf","12","-pix_fmt","yuv420p","-an",out],check=True)
    print("crop", out, "box", x0, y0, size, "->", outpx)

def paste(src, cropped, out, cx, cy, size, feather=40):
    w,h,fr,dur = probe(src); x0 = max(0, min(w-size, cx-size//2)); y0 = max(0, min(h-size, cy-size//2))
    # máscara cuadrada con borde suave (feather px) hecha con geq sobre un lienzo gris
    f = feather
    mask = (f"color=c=white:s={size}x{size},format=gray,"
            f"geq=lum='255*min(1,min(min(X,{size}-1-X),min(Y,{size}-1-Y))/{f})'")
    fc = (f"[1:v]scale={size}:{size}:flags=lanczos,fps={fr},setpts=PTS-STARTPTS[c];"
          f"{mask}[m];[c][m]alphamerge[ca];"
          f"[0:v][ca]overlay={x0}:{y0}:format=auto:shortest=1[v]")
    subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-i",cropped,"-filter_complex",fc,"-map","[v]","-map","0:a?","-c:v","libx264","-crf","12","-pix_fmt","yuv420p","-c:a","copy",out],check=True)
    print("paste", out)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "crop":
        src, out, box = sys.argv[2:5]; cx,cy,size = map(int, box.split(",")); outpx = int(sys.argv[sys.argv.index("--out")+1]) if "--out" in sys.argv else 1280
        crop(src, out, cx, cy, size, outpx)
    elif cmd == "paste":
        src, cropped, out, box = sys.argv[2:6]; cx,cy,size = map(int, box.split(",")); fe = int(sys.argv[sys.argv.index("--feather")+1]) if "--feather" in sys.argv else 40
        paste(src, cropped, out, cx, cy, size, fe)
    else:
        print(__doc__)
