#!/usr/bin/env python3
"""Cama musical V1 (horror_v1_elevenlabs, 60 s): RMS parejo (level de music_bed) + envolvente fija sin ducking.
  intro: 0.40 → cuerpo oscuro: 0.18 (sube suave a 0.25 hacia c7) → APAGÓN: silencio → showroom: 0.13 → tras la última palabra: 0.70 · mezcla final loudnorm −16 LUFS → fade final.
Uso: python tools/musica_v1.py video_in video_out
"""
import sys, os, json, subprocess, numpy as np
sys.path.insert(0,"tools"); from music_bed import level, _load, SR
vin,vout=sys.argv[1],sys.argv[2]
tl=json.load(open(sys.argv[3] if len(sys.argv)>3 else "build/v1/timeline.json")); parts={p["name"]:p for p in tl["parts"]}; total=tl["total"]
intro_end=(parts["negro"] if "negro" in parts else parts["c1"])["start"]; ap=parts["APAGON"]; c7=parts["c7"]; c8a=parts["c8a"]
last_word=41.04+parts["c8b"]["offset"]   # «terraregia.com» termina
m=level(_load("media/09_musica/horror_v1_elevenlabs.mp3",0.0,min(60.0,total+0.5)))
if len(m)<int(SR*total): m=np.concatenate([m,np.zeros((int(SR*total)-len(m),2),"float32")])
m=m[:int(SR*total)]; t=np.arange(len(m))/SR
env=np.full(len(t),0.18)
env[t<intro_end]=0.40
seg=(t>=intro_end)&(t<c7["start"]+c7["dur"]); env[seg]=0.18+0.07*np.clip((t[seg]-intro_end)/max(c7["start"]+c7["dur"]-intro_end,1),0,1)
env[(t>=ap["start"])&(t<ap["start"]+ap["dur"])]=0.0
env[(t>=c8a["start"])&(t<last_word)]=0.13
env[t>=last_word]=0.70
# suavizar transiciones (0.35 s) salvo la caída del apagón, que es seca (0.08 s)
k=int(SR*0.35); ker=np.ones(k)/k; envs=np.convolve(np.pad(env,k//2,mode="edge"),ker,mode="valid")[:len(env)]
cut=(t>=ap["start"]-0.08)&(t<ap["start"]+ap["dur"]); envs[cut]=np.minimum(envs[cut],np.where(t[cut]<ap["start"],(ap["start"]-t[cut])/0.08*0.25,0.0))
envs*=np.clip(t/0.4,0,1)*np.clip((total-t)/0.9,0,1)
y=np.clip(m*envs[:,None],-1,1).astype("float32")
subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-f","f32le","-ac","2","-ar",str(SR),"-i","-","-c:a","pcm_s16le",(os.path.dirname(sys.argv[3])+"/musica_bed.wav" if len(sys.argv)>3 else "build/v1/musica_bed.wav")],input=y.tobytes(),check=True)
subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-i",vin,"-i",(os.path.dirname(sys.argv[3])+"/musica_bed.wav" if len(sys.argv)>3 else "build/v1/musica_bed.wav"),"-filter_complex","[0:a][1:a]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]","-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",vout],check=True)
print("ok",vout,"última palabra",round(last_word,2),"total",total)
