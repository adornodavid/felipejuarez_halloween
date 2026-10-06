#!/usr/bin/env python3
"""c1 con ENCENDIDO real: antepone HOLD s del primer cuadro a oscuras y aplica curva de ganancia (clic de linterna).
Uso: encendido.py in.mp4 out.mp4 [hold=1.0] [click=0.75]"""
import sys, subprocess, numpy as np
src, out = sys.argv[1], sys.argv[2]
HOLD = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
CLICK = float(sys.argv[4]) if len(sys.argv) > 4 else 0.75
pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split(",")
w, h = int(pr[0]), int(pr[1]); num, den = pr[2].split("/"); fps = int(num) / int(den)
nh = int(round(HOLD * fps)); kc = int(round(CLICK * fps))

def gain(i):
    if i < kc: return 0.03
    if i == kc: return 0.7      # destello del clic
    if i == kc + 1: return 0.08  # rebote
    j = i - (kc + 2)
    return min(1.0, 0.35 + 0.65 * j / 4) if j < 4 else 1.0

dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", out + ".video.mp4"], stdin=subprocess.PIPE)
first = dec.stdout.read(w * h * 3); f0 = np.frombuffer(first, np.uint8).astype(np.float32)
for i in range(nh):
    enc.stdin.write((f0 * gain(i)).clip(0, 255).astype(np.uint8).tobytes())
i = nh; buf = first
while len(buf) == w * h * 3:
    g = gain(i)
    if g < 1:
        enc.stdin.write((np.frombuffer(buf, np.uint8).astype(np.float32) * g).clip(0, 255).astype(np.uint8).tobytes())
    else:
        enc.stdin.write(buf)
    i += 1; buf = dec.stdout.read(w * h * 3)
enc.stdin.close(); enc.wait()
# audio: room tone HOLD s + clic sintético en CLICK + audio original
ms = int(CLICK * 1000)
subprocess.run(["ffmpeg", "-v", "error", "-y",
    "-f", "lavfi", "-i", "anoisesrc=color=pink:amplitude=0.0025:r=48000,aformat=channel_layouts=stereo",
    "-f", "lavfi", "-i", "anoisesrc=color=white:amplitude=0.6:r=48000,aformat=channel_layouts=stereo",
    "-i", src,
    "-filter_complex", f"[0:a]atrim=0:{HOLD}[rt];[1:a]atrim=0:0.02,afade=t=out:st=0.004:d=0.016,adelay={ms}|{ms},apad=whole_dur={HOLD}[ck];[rt][ck]amix=inputs=2:normalize=0[pre];[2:a]aformat=sample_rates=48000:channel_layouts=stereo[o];[pre][o]concat=n=2:v=0:a=1[a]",
    "-map", "[a]", "-c:a", "pcm_s16le", out + ".audio.wav"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out + ".video.mp4", "-i", out + ".audio.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)
print("ok", out)
