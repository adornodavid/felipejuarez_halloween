#!/usr/bin/env python3
"""Montaje V3 (6-oct noche, toma por toma aprobada): intro 6 s → c1 encendido → c2 v3 → c3a v3 → c3b v3 → c4 v3 → c5 → c6 v3 (manos avatar) → c7 v3
→ APAGÓN 2.5 s → insert mesa (luces suben) → c8 zoom (desde t=IN8) → outro 3 s.
Voz: UNA pista continua `media/07_voz/voz_Jonas_sts_v3_42s.mp3` mapeada por tramos (sin cortes clip a clip). Escribe build/v3/timeline.json.
Uso: montaje_v3.py [salida=build/v3/v3_cuerpo_sin_musica.mp4]"""
import subprocess, json, sys, os
OUT=sys.argv[1] if len(sys.argv)>1 else "build/v3/v3_cuerpo_sin_musica.mp4"; os.makedirs("build/v3",exist_ok=True)
VOZ="media/07_voz/voz_Jonas_sts_v3_42s.mp3"; INS=1.4; IN8=1.4
# (nombre, archivo, inicio en el crudo/voz, dur o None=todo)
parts=[("intro","build/v2/intro.mp4",None,6.0),
 ("c1","build/clips/c1_felipe_encendido.mp4",-0.06,None),("c2","build/clips/c2_felipe_v3.mp4",6.54,None),
 ("c3a","build/clips/c3a_felipe_v3.mp4",8.46,None),("c3b","build/clips/c3b_felipe_v3.mp4",13.0,None),
 ("c4","build/clips/c4_felipe_v3.mp4",19.79,None),("c5","build/clips/c5_felipe.mp4",22.29,None),
 ("c6","build/clips/c6_mano_v3_mudo.mp4",26.54,None),("c7","build/clips/c7_felipe_v3.mp4",28.08,None),
 ("APAGON","build/v2/apagon.mp4",None,2.5),("c8ins","build/clips/c8a_insert_v3_mudo.mp4",32.58,INS),
 ("c8","build/clips/c8_felipe_v3.mp4",32.58+IN8,None),("outro","build/v2/outro.mp4",None,3.0)]
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())
t=0; tl=[]; vf=[]; af=[]; inputs=[]
for i,(n,f,orig,d) in enumerate(parts):
    D=d if d else dur(f); inputs+=["-i",f]
    seek=f"trim=start={IN8},setpts=PTS-STARTPTS," if n=="c8" else ""
    vf.append(f"[{i}:v]{seek}scale=1080:1920,fps=30,setsar=1,trim=duration={D:.4f},setpts=PTS-STARTPTS[v{i}]")
    tl.append({"name":n,"start":round(t,4),"dur":round(D,4),"orig":orig,"offset":(round(t-orig,4) if orig is not None else None)}); t+=D
# voz: tramos continuos (sin clip a clip). Segmentos: [6.0 .. 37.6) ← voz desde -0.06 ; apagón silencio ; insert+c8 ← voz desde 32.58
v_start=tl[1]["start"]; v_len=sum(p["dur"] for p in tl[1:9]); a_start=tl[10]["start"]; a_len=tl[10]["dur"]+tl[11]["dur"]
afilt=(f"[{len(parts)}:a]atrim=start=0:duration={v_len:.4f},asetpts=PTS-STARTPTS,adelay={int(v_start*1000)}|{int(v_start*1000)},aformat=sample_rates=48000:channel_layouts=stereo[va];"
       f"[{len(parts)+1}:a]atrim=start=32.58:duration={a_len:.4f},asetpts=PTS-STARTPTS,adelay={int(a_start*1000)}|{int(a_start*1000)},aformat=sample_rates=48000:channel_layouts=stereo[vb];"
       f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=duration=6,asetpts=PTS-STARTPTS[ia];[ia][va][vb]amix=inputs=3:normalize=0,apad=whole_dur={t:.3f}[a]")
fc=";".join(vf)+";"+"".join(f"[v{i}]" for i in range(len(parts)))+f"concat=n={len(parts)}:v=1:a=0[v];"+afilt
cmd=["ffmpeg","-v","error","-y"]+inputs+["-i",VOZ,"-i",VOZ,"-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-crf","12","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-t",f"{t:.3f}",OUT]
subprocess.run(cmd,check=True); json.dump({"total":round(t,3),"parts":tl},open("build/v3/timeline.json","w"),indent=1)
print("ok",OUT,round(t,2),"s"); [print(f"  {p['name']:7s} {p['start']:7.2f} +{p['dur']:.2f}") for p in tl]
