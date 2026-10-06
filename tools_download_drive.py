#!/usr/bin/env python3
"""Baja a media/ todo el material de Drive del proyecto (ids del repo de Rudy + carpeta Personaje de David). Idempotente: salta lo que ya existe."""
import os, gdown
L = {
 "media/05_intro": [("1d-d0542NERJeQQou-YoUQKHhURkVH5Vi","intro_le-temes-a-invertir_story.mp4")],
 "media/01_crudos_chroma_4k": [("1kcdjxLiRQcE9c6ie_txcRvxw6mGtS4aL","IMG_0303.MOV"),("1B1SFRETqUNe-FP6-LBqzFuxeYWofW9j3","IMG_0310.MOV"),("1KHZ-O0VHruU_trggKQkonbvcCPvaKUwZ","IMG_0311.MOV"),("1-rHxwFWFFdhHeO0rV39Z1CNBMyuwQFm_","IMG_0313.MOV"),("12_Hh3SLj_3jEVZUej9Ue9jzr7BkYbGjl","IMG_0314.MOV"),("1hABAdOj7AHvM3q_UQ-VBzkhvFrTovg0l","IMG_0315.MOV"),("1HWF5dC-IzsblEZE8QCnjnSJqHjVcW4X_","IMG_0318.MOV"),("1D59veMLrew1BP6XcFu58t619Fne48kXU","IMG_0319.MOV"),("1A7R2vHwgkIrqjdmfbndV6aDHaWqR_tVz","IMG_0321.MOV"),("1WSX8rEcAMH-RuaiInyIYFG0HqkzzyGJp","IMG_0322.MOV")],
 "media/02_crudos_otro_angulo": [("1iRyuAR5piEfya55zN4n6Bmm8YBKaVac4","IMG_8507.MOV"),("1j23b-fKUaivJfarZhfrWSbCX3WHDSYmE","IMG_8515.MOV"),("1C-h1U0i83SH7jJU9Hmz2aGVoGmmxzbPb","IMG_8516.MOV"),("1bAdfk6FSiR5n-Pq3DA9oF8Qo9lsp8OB3","IMG_8517.MOV")],
 "media/03_cortes_720p": [("1swQ4Cr2ZMB_4fCCRZzlI4TVtpPnhu6wi","1_de_8.mp4"),("180DmihlTU1w5lpw84qIk1CooN94nYTwm","2_de_8.mp4"),("1oFTFS06eiqunzshy8hqTZ8tX1ZTLrvtH","3_de_8.mp4"),("1zp_QQ5LJCFNPx4VxIuKJ1aWBmJW-hEKn","4_de_8.mp4"),("1vzjfMMyczs0EEeCvpWC1hpW5fRxkYvo5","5_de_8.mp4"),("1scj0URkZqWBw-CBL-yLDZcyqVa07HZwv","6_de_8.mp4"),("14xCUgdbWZaH5PSiV-WQ9EgtF3-47u6gO","7_de_8.mp4"),("1Dpq_JJsq6VwGaZ3Fpmq83y3RVTCNXyfV","8_de_8.mp4"),("1h3ku1YBdNYpfUt4JOcZs2LZaUkxpZCBs","Video_Final_David.mp4"),("1ILVkQp6pmCHVENk9LHFHWFqf2v6wi5il","Video_Solo_voz_David.mp4")],
 "media/07_voz": [("1U1wG9dsOEDEcqV3lB4edAybZk2ZY6bai","voz_original_David.wav"),("1TH9tTSMQaaQS5yZTgTMhGjWVtfoBObJh","voz_Jonas_sts.mp3"),("1yoLabeyDc36Bmx3sKj5OqpfRQpPLotQe","Video_Solo_voz_Jonas.mp4")],
 "media/06_personaje": [("1tvCuty-dMIltKWP3faHhV3rMxY7-paxF","felipe2_3_vistas_faceless_ceja_arreglo.png"),("1D6CB6zXVAu93bop0w6-c48RLDEd2eBKZ","felipe2_3_vistas_faceless.jpg"),("17nbmW83PZ3dnAX9MFWMGostyCPNHCXkZ","felipe2_3_vistas.png"),("1WE4SNp_aWtE3pJaYgKsL4NSSOC3DuGX9","felipe2_1_closeup_rostro.png"),("1x8uuQIndr1ywJtueqsNi4ojb-cBCbihf","felipe2_2_cuerpo_frente.png"),("1P6-2eXa2-uGXAeRhjwiXpFAgajgO4ZOr","felipe2_3_cuerpo_espalda.png")],
 "media/06_personaje/props": [("1ZKP4a485KDgY2jU2GKAGC4qEvDxIJIht","linterna_1_closeup_frente.png"),("1c5oMccLbWR9UEic4xEaIGxxbEbHhMs1u","linterna_2_completa_lado.png"),("13qpURAUiCMyft0EK_4EgOHSm6OGKjWs0","mesa_alta_completa.png"),("1yqsdbhAtsK9nVW4zdJWFJO9XBlIk-jSA","sillon_1_tres_cuartos.png"),("1jpQh1Eq0YUEkbOXGcTAmWqoKCLmie3pq","sillon_2_perfil.png")],
 "media/06_personaje/refs_luz": [("1vsw7zhz7r2FZGIm2DuaK0POApX2aEfMf","ref_luz_clip1_v3.png"),("1lgPk6qPa6sdvwWGiiIxPl_UYyleal6r2","compara_luz_clip1_vs_3.png"),("1Y_y2ldc6Ln_NEltQH4wbGv0MhgeR2I9T","compara_luz_clip1_vs_5_7_v3.png")],
 "media/08_genjutsu_rudy": [("1a4pxtqk4t7bhbfFAVLZdazSrcBGKhmDV","clip_1_genjutsu_720p_v3.mp4"),("13-4YQ7irBY1Lf9PxPWxphO9ok37_123b","clips_2_4_6_genjutsu_720p.mp4"),("1-ObKwEM8pEO7qp5AdbngeDG2kb9_UNqV","clip_3_genjutsu_720p.mp4"),("1_ZHUC6V63UVmR2rNSgfkoldOoqikfLwe","clips_5_7_genjutsu_720p_v3.mp4"),("1ET5H1vaqGHcVzgYuX1q2cyxXwsUCiTjF","clip_8_genjutsu_720p_sin_silla.mp4"),("1RoMaCoKNlTu51Fpu-IUcYH2uHBh1W3me","clip_8_genjutsu_720p.mp4"),("12EsZtfHW_IA_eWjyx5fGpG7Nw-OWq_F-","quitar_silla_clip8.py")],
 "media/04_referencia_resultado": [("1PA4McX0Gx9lM_n0vdvp2MhQpgmM-0x-Y","Felipe_1.0_DESCARTADO_solo_ref.mp4"),("14aEH95xAdlNp_0bb7Tovt_Ai2yPAih1S","Referencia_chroma_studio_David.mp4"),("1AgmdsuLwPC6tMSQkM7ymztTI9ZnNuK2T","Referencia_video_TerraRegia_Video1.mp4")],
}
for d, items in L.items():
    os.makedirs(d, exist_ok=True)
    for fid, name in items:
        p = os.path.join(d, name)
        if os.path.exists(p) and os.path.getsize(p) > 0: print("ya", p); continue
        try: gdown.download(id=fid, output=p, quiet=True); print("ok", p, os.path.getsize(p)//1_000_000, "MB", flush=True)
        except Exception as e: print("FALLÓ", p, str(e)[:120], flush=True)
print("FIN")
