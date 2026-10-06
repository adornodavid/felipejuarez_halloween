# Compone el croma sobre un render A ESCALA: python comp.py toma.mp4 render.jpg salida.mp4 cropx0,cropy0,cropx1,cropy1(frac) piesx,piesy(frac del crop) altura(frac del crop)
import sys, subprocess, numpy as np
from PIL import Image, ImageFilter
Image.MAX_IMAGE_PIXELS=None
src, render, out = sys.argv[1:4]
x0,y0,x1,y1 = map(float, sys.argv[4].split(",")); fx,fy = map(float, sys.argv[5].split(",")); hfrac=float(sys.argv[6])
OW,OH=1080,1920
R=Image.open(render).convert("RGB"); W,H=R.size
bg=np.asarray(R.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H))).resize((OW,OH),Image.LANCZOS)).astype(np.float32)
pr=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate","-of","csv=p=0",src],capture_output=True,text=True).stdout.strip().split(",")
w,h=int(pr[0]),int(pr[1]); fps=pr[2]
def alpha(f):
    f=f.astype(np.float32); d=f[...,1]-np.maximum(f[...,0],f[...,2]); return 1-np.clip((d-18)/38,0,1)
# bbox de la persona en el primer cuadro (para escala estable)
first=subprocess.run(["ffmpeg","-v","error","-i",src,"-frames:v","1","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
a0=alpha(np.frombuffer(first,np.uint8).reshape(h,w,3)); ys=np.where((a0>0.5).sum(1)>0.03*w)[0]; xs=np.where(a0.max(0)>0.5)[0]
top,bot=ys.min(),ys.max(); cxp=(xs.min()+xs.max())/2
s=(hfrac*OH)/(bot-top); nw,nh=int(w*s),int(h*s)
ox=int(fx*OW-cxp*s); oy=int(fy*OH-bot*s)
print("escala",round(s,2),"persona px",int((bot-top)*s),"offset",ox,oy)
dec=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
enc=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{OW}x{OH}","-r",fps,"-i","-","-i",src,"-map","0:v","-map","1:a","-c:v","libx264","-crf","14","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest",out],stdin=subprocess.PIPE)
# sombra de contacto suave bajo los pies
while True:
    buf=dec.stdout.read(w*h*3)
    if len(buf)<w*h*3: break
    f=Image.fromarray(np.frombuffer(buf,np.uint8).reshape(h,w,3)).resize((nw,nh),Image.LANCZOS)
    fa=np.asarray(f).astype(np.float32); a=alpha(fa); a[int(bot*s)+1:,:]=0
    # cinta amarilla del piso del foro: naranja/amarillo saturado en el 12% inferior de la persona
    lo=int((top+(bot-top)*0.88)*s); r_,g_,b_=fa[lo:,...,0],fa[lo:,...,1],fa[lo:,...,2]
    tape=(r_>150)&(g_>100)&(b_<110)&((r_-b_)>90)&((g_-b_)>50); a[lo:][tape]=0
    a=np.asarray(Image.fromarray((a*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1))).astype(np.float32)/255
    d=fa[...,1]-np.maximum(fa[...,0],fa[...,2]); fa[...,1]=np.where(d>0,np.maximum(fa[...,0],fa[...,2])+d*0.15,fa[...,1])
    o=bg.copy()
    # sombra elíptica
    sh=np.zeros((OH,OW),np.float32); yy,xx=np.ogrid[:OH,:OW]; cy=fy*OH; rx=0.11*hfrac*OH; ry=0.012*hfrac*OH
    sh=np.clip(1-(((xx-fx*OW)/rx)**2+((yy-cy)/ry)**2),0,1)*0.45; o*= (1-sh[...,None])
    X0,Y0=max(ox,0),max(oy,0); X1,Y1=min(ox+nw,OW),min(oy+nh,OH)
    sub=fa[Y0-oy:Y1-oy, X0-ox:X1-ox]; sa=a[Y0-oy:Y1-oy, X0-ox:X1-ox,None]
    o[Y0:Y1,X0:X1]=sub*sa+o[Y0:Y1,X0:X1]*(1-sa)
    enc.stdin.write(o.clip(0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print("ok",out)
