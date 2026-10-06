#!/usr/bin/env python3
"""Subtítulos de CINE para Felipe Juárez: una línea serif (Minion Pro), blanco 92 %, sombra suave, tinta POR PALABRA
(la palabra que suena se tiñe ámbar linterna). Frases del guion partidas para que quepan en una línea (≤ 920 px).
Tiempos: palabras de David (scribe) + offset por clip de build/v1/timeline.json. Tinta oscura automática sobre fondo claro.
Uso: python tools/subs_cine.py in.mp4 out.mp4 [y0=1430]
"""
import json, os, subprocess, sys, io, unicodedata
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30; MAXW=920; SIZE=58; AMBER=(242,193,78); WHITE=(255,255,255); DARK=(31,45,59)
FONT=os.path.expanduser("~/Proyectos/terraregia-ads-proyectos/public/fonts/MinionPro-Regular.otf")
B="build/subscine"; os.makedirs(B,exist_ok=True)
def norm(s): return "".join(c for c in unicodedata.normalize("NFD",s.lower()) if unicodedata.category(c)!="Mn").strip('.,:;¿?¡!"«»')
PHRASES=["Vio el terreno, le gustó.","Dijo: «Lo pienso, te aviso».","Nunca me avisó.","Nunca volvió a contactarme.","Tiempo después,",
 "buscó el mismo terreno,","pero ya no estaba disponible.","Estaba a nombre de alguien","que sí tomó la decisión.","¿Y el terreno?",
 "El terreno ya había duplicado su valor.","Lo que da miedo","es dejar pasar oportunidades.","En Terra Regia tenemos el terreno",
 "donde tu dinero sí crece.","Conoce más en terraregia.com"]
words=[w for w in json.load(open("media/04_referencia_resultado/david_words.json"))["words"] if w["type"]=="word"]
tl=json.load(open("build/v1/timeline.json"))["parts"]
def newtime(t):
    for p in tl:
        if p["name"]!="APAGON" and p.get("orig") is not None and p["orig"]-0.05<=t<p["orig"]+p["dur"]+0.05: return t+p["offset"]
    return None
f=ImageFont.truetype(FONT,SIZE); tmp=ImageDraw.Draw(Image.new("RGBA",(10,10)))
def wbox(t): bb=tmp.textbbox((0,0),t,font=f); return bb[2]-bb[0], bb[3]-bb[1], bb
i=0; phrases=[]
for ph in PHRASES:
    toks=ph.split(); row=[]
    for tok in toks:
        if i>=len(words): raise SystemExit("faltan palabras")
        if norm(tok)!=norm(words[i]["text"]): print(f"⚠️ «{tok}» ≠ scribe «{words[i]['text']}»")
        row.append((tok,words[i]["start"],words[i]["end"])); i+=1
    phrases.append(row)
if i!=len(words): print("⚠️ sobran palabras:",[w["text"] for w in words[i:]])
src,out=sys.argv[1],sys.argv[2]; y0=int(sys.argv[3]) if len(sys.argv)>3 else 1430
L=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src],capture_output=True,text=True).stdout)
ov=[]
for pi,row in enumerate(phrases):
    a=newtime(row[0][1]); b=newtime(row[-1][2])
    if a is None or b is None: print("⚠️ frase fuera de timeline:",row); continue
    fin=b+0.45
    if pi+1<len(phrases):
        na=newtime(phrases[pi+1][0][1])
        if na: fin=min(fin,na-0.04)
    # layout de la línea
    sp=int(SIZE*0.27); xs=[]; x=0
    for tok,_,_ in row: w_,h_,_=wbox(tok); xs.append((x,w_)); x+=w_+sp
    lw=x-sp; x0=(W-lw)//2
    if lw>MAXW: print(f"⚠️ frase {pi} ancha: {lw}px")
    # contraste
    fr=subprocess.run(["ffmpeg","-v","error","-ss",f"{a+0.1:.2f}","-i",src,"-frames:v","1","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    reg=Image.open(io.BytesIO(fr)).convert("L").crop((max(x0,0),y0-10,min(x0+lw,W),y0+SIZE+20)); lum=float(np.percentile(np.asarray(reg),70)); dark=lum>140
    base=DARK if dark else WHITE
    print(f"frase {pi:>2} {a:6.2f}–{fin:6.2f} lum {lum:3.0f} {'OSCURA' if dark else 'blanca'}  {' '.join(t for t,_,_ in row)}")
    # un PNG por estado (palabra k teñida); estado -1 = ninguna teñida (antes de que arranque la primera ya es la 0)
    states=[]
    for k,(tok,ws,we) in enumerate(row):
        s=newtime(ws); states.append((k,s))
    states.append((len(row),fin))
    for k in range(len(row)):
        im=Image.new("RGBA",(W,SIZE+80),(0,0,0,0))
        sh=Image.new("RGBA",(W,SIZE+80),(0,0,0,0)); dsh=ImageDraw.Draw(sh)
        for j,(tok,_,_) in enumerate(row):
            dsh.text((x0+xs[j][0]+3,40+5),tok,font=f,fill=(255,255,255,110) if dark else (0,0,0,190))
        sh=sh.filter(ImageFilter.GaussianBlur(8)); d=ImageDraw.Draw(im)
        for j,(tok,_,_) in enumerate(row):
            col=AMBER if j==k else base; al=255 if j<=k else 215
            d.text((x0+xs[j][0],40),tok,font=f,fill=col+(al,))
        png=f"{B}/p{pi}_{k}.png"; Image.alpha_composite(sh,im).save(png)
        t0=max(states[k][1],a); t1=states[k+1][1]
        if k==0: t0=a
        ov.append((png,0,y0-40,t0,max(t1,t0+1/FPS)))
fc="[0:v]null[base]"; cur="base"; inputs=[]
for n,(p,x,y,a,b) in enumerate(ov):
    inputs+=["-loop","1","-i",os.path.abspath(p)]
    fc+=f";[{cur}][{n+1}:v]overlay={x}:{y}:enable='between(t,{a:.3f},{b:.3f})':format=auto[v{n}]"; cur=f"v{n}"
fc+=f";[{cur}]format=yuv420p[v]"
subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-i",src]+inputs+["-filter_complex",fc,"-map","[v]","-map","0:a","-t",f"{L:.3f}","-c:v","libx264","-crf","15","-r",str(FPS),"-c:a","copy",out],check=True)
print("ok",out,len(ov),"overlays")
