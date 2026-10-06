#!/bin/zsh
# uso: tools/finish_clip.sh <clip> <url_lipsync>  → build/clips/<clip>_felipe.mp4 (Kling 1080p + boca lipsync pegada + voz)
set -e
c=$1; u=$2
box=$(awk -v c=$c '$1==c{print $2}' build/crops/boxes.txt)
k=build/kling/${c}_kling_1080p.mp4; [ -f build/kling/${c}_kling_1080p_trim.mp4 ] && k=build/kling/${c}_kling_1080p_trim.mp4
v=build/test/voz_$c.wav; [ $c = c1 ] && v=build/test/voz_jonas_v3_clip1_roomtone.wav
curl -sS -L -o build/lipsync/${c}_crop_ls.mp4 "$u" </dev/null
python3 tools/facecrop.py paste $k build/lipsync/${c}_crop_ls.mp4 build/clips/${c}_mudo.mp4 $box --feather 48 </dev/null
ffmpeg -nostdin -v error -y -i build/clips/${c}_mudo.mp4 -i $v -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest build/clips/${c}_felipe.mp4
echo "$c listo: $(ffprobe -v error -show_entries format=duration -of csv=p=0 build/clips/${c}_felipe.mp4) s  caja $box"
