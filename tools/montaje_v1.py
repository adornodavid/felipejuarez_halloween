#!/usr/bin/env python3
"""Montaje Versión 1 — sigue el storyboard aprobado (5-oct).
Timeline (1080×1920 · 30 fps · 48 kHz st):
  [intro cerillo 6 s] → negro 1 s → c1 (encendido 3 cuadros) → c2 c3a c3b c4 c5 c6(mano) c7 → APAGÓN 2.5 s → c8a (luces 0.6 s) → c8b → outro logo TR 3 s
Escribe build/v1/timeline.json con el offset de cada clip (nuevo_inicio − inicio_en_el_crudo) para los subtítulos.
"""
import subprocess, json, os, sys
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1080,1920,30; OUT="build/v1"; os.makedirs(OUT,exist_ok=True)
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())
def run(c): subprocess.run(c,check=True)
INTRO = sys.argv[1] if len(sys.argv)>1 and os.path.exists(sys.argv[1]) else None
# (nombre, archivo, inicio en el crudo de David, fade-in s)
CLIPS=[("c1","build/clips/c1_felipe.mp4",0.94,3/FPS),("c2","build/clips/c2_felipe.mp4",6.54,0),("c3a","build/clips/c3a_felipe.mp4",8.46,0),
       ("c3b","build/clips/c3b_felipe.mp4",13.0,0),("c4","build/clips/c4_felipe.mp4",19.79,0),("c5","build/clips/c5_felipe.mp4",22.29,0),
       ("c6","build/clips/c6_mano_mudo.mp4",26.54,0),("c7","build/clips/c7_felipe.mp4",28.08,0),
       ("APAGON",None,None,0),("c8a","build/clips/c8a_felipe.mp4",32.58,0.6),("c8b","build/clips/c8b_felipe.mp4",37.5,0)]
ROOM="anoisesrc=color=pink:amplitude=0.0025:r=48000,aformat=channel_layouts=stereo"
def black(sec,name):
    p=f"{OUT}/{name}.mp4"; run(["ffmpeg","-nostdin","-v","error","-y","-f","lavfi","-i",f"color=c=black:s={W}x{H}:r={FPS}:d={sec}","-f","lavfi","-i",ROOM,"-t",str(sec),"-c:v","libx264","-crf","14","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest",p]); return p
def norm(src,name,fade=0):
    """Escala/recorta a 1080×1920, 30 fps, audio 48k estéreo (room tone si no trae audio)."""
    p=f"{OUT}/{name}.mp4"; d=dur(src)
    has_a=subprocess.run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=codec_type","-of","csv=p=0",src],capture_output=True,text=True).stdout.strip()!=""
    vf=f"scale={W}:-2:flags=lanczos,crop={W}:{H},fps={FPS},format=yuv420p"+(f",fade=t=in:st=0:d={fade}" if fade else "")
    cmd=["ffmpeg","-nostdin","-v","error","-y","-i",src]
    if not has_a: cmd+=["-f","lavfi","-i",ROOM]
    cmd+=["-filter:v",vf,"-map","0:v","-map",("1:a" if not has_a else "0:a"),"-t",f"{d:.3f}","-c:v","libx264","-crf","14","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",p]
    run(cmd); return p
def outro(sec=3.0):
    logo=Image.open(os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/logos/TR_white.png")).convert("RGBA")
    lw=560; logo=logo.resize((lw,int(logo.height*lw/logo.width)),Image.LANCZOS)
    im=Image.new("RGBA",(W,H),(0,0,0,255)); im.alpha_composite(logo,((W-lw)//2,H//2-logo.height-30))
    f=ImageFont.truetype(os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/fonts/HELVETICANOWDISPLAY-MEDIUM.TTF"),46)
    d=ImageDraw.Draw(im); t="terraregia.com"; bb=d.textbbox((0,0),t,font=f); d.text(((W-(bb[2]-bb[0]))//2,H//2+50),t,font=f,fill=(255,255,255,235))
    im.convert("RGB").save(f"{OUT}/outro.png")
    p=f"{OUT}/outro.mp4"; run(["ffmpeg","-nostdin","-v","error","-y","-loop","1","-i",f"{OUT}/outro.png","-f","lavfi","-i",ROOM,"-t",str(sec),"-vf",f"fps={FPS},format=yuv420p,fade=t=in:st=0:d=0.5,fade=t=out:st={sec-0.6}:d=0.6","-c:v","libx264","-crf","14","-c:a","aac","-b:a","192k","-shortest",p]); return p
parts=[]; tl=[]; t=0.0
if INTRO:
    p=norm(INTRO,"intro"); di=dur(p)
    if di>6.2: run(["ffmpeg","-nostdin","-v","error","-y","-i",p,"-t","6.0","-af","afade=t=out:st=5.4:d=0.6","-c:v","libx264","-crf","14","-c:a","aac","-b:a","192k",f"{OUT}/intro6.mp4"]); p=f"{OUT}/intro6.mp4"
    parts.append(p); tl.append(dict(name="intro",start=t,dur=dur(p))); t+=dur(p)
p=black(1.0,"negro_inicio"); parts.append(p); tl.append(dict(name="negro",start=t,dur=1.0)); t+=1.0
for name,src,orig,fade in CLIPS:
    if name=="APAGON": p=black(2.5,"apagon"); d=2.5; orig=31.58
    else: p=norm(src,f"n_{name}",fade); d=dur(p)
    parts.append(p); tl.append(dict(name=name,start=round(t,3),dur=round(d,3),orig=orig,offset=round(t-orig,3))); t+=d
p=outro(); parts.append(p); tl.append(dict(name="outro",start=t,dur=3.0)); t+=3.0
with open(f"{OUT}/concat.txt","w") as f:
    for p in parts: f.write(f"file '{os.path.abspath(p)}'\n")
run(["ffmpeg","-nostdin","-v","error","-y","-f","concat","-safe","0","-i",f"{OUT}/concat.txt","-c:v","libx264","-crf","14","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-movflags","+faststart",f"{OUT}/v1_cuerpo_sin_musica.mp4"])
json.dump(dict(total=round(t,3),parts=tl),open(f"{OUT}/timeline.json","w"),indent=1,ensure_ascii=False)
print("total",round(t,2),"s"); [print(f"  {x['name']:<7} {x['start']:>6.2f} +{x['dur']:.2f}"+(f"  offset {x['offset']:+.2f}" if 'offset' in x and x['offset'] is not None else "")) for x in tl]
