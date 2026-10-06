# Prompts Genjutsu — Felipe Juarez 1.0

Texto exacto enviado a Higgsfield, recuperado del historial de generaciones (5 oct 2026). En `medias` el orden = número de "reference image N" del prompt.

## Felipe 1.0 · Clip 1 (encendido) — usado

- job_id: `5f5f2f16-e795-4525-ae38-1e5205cb66bf`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 7 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`8e7a0d2d-671f-4c87-ab2d-5f184deac1c2` (media_input), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`f1273ca2-7311-4dad-84d3-3fe986dd115f` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261001_040423_5f5f2f16-e795-4525-ae38-1e5205cb66bf.mp4

```text
1) NO subtitles, NO captions, NO words, NO text of any kind anywhere on screen, in any frame.
2) FRAMING: keep exactly the same close framing as the source video: same camera distance, same crop, same head size and position, his head near the top and his hands with the object at the bottom center. Do NOT zoom out, do NOT widen the shot, do NOT show his legs or the chair.
3) Keep body movement, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
4) Replace the microphone with the flashlight from reference image 3, held the same way with both hands, its lens pointing up toward his face.
5) Replace the man with the man from reference images 1 and 2: same face, gray hair and gray beard, very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, wristwatch on his left wrist, no bracelets. Same lip movements as the original man.
6) DARKNESS AND FLASHLIGHT: the room is completely dark, pitch black, nothing of the room is visible, no green anywhere. The video starts in darkness with the flashlight OFF: his silhouette is only barely visible in the dark. Then, before he starts talking, he switches the flashlight ON and the light visibly comes on and reveals his face. From then the only light is the flashlight shining upward from below onto his face, with the same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. The light on his face is soft and well exposed, NOT blown out and NOT overexposed: his facial features, skin texture, gray beard and identity stay clearly readable, with no light patterns or textures projected on his face.
7) His body stays very dark: the shirt, the t-shirt and the arms are almost black, only his hands catch a faint glow near the flashlight. Only the face is clearly lit.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN (complementary full-body and face views of the same man): light-to-medium skin, swept-back gray hair with darker undertones, neatly groomed gray beard and mustache, mature facial features, average build. Wardrobe: very dark bottle-green flannel button-down shirt worn open over a white crew-neck T-shirt, left-wrist watch, no bracelets.
@Image3 — FLASHLIGHT, the replacement FLASHLIGHT: matte black handheld flashlight with a broad cylindrical lens head, textured grip, and dark end cap.
@Image4 — UNDER-LIGHTING, the LIGHTING REFERENCE: pitch-black surrounding darkness with a soft, controlled upward flashlight illumination that reveals the lower face while casting deep shadow across the eyes and forehead.
Video edit. Keep this @Video1 clip exactly as it is — the same single continuous 0-6s shot, static camera, close portrait framing, crop, head size and position, with the head near the top and both hands holding the object at bottom center; do not widen, zoom out, show legs, or reveal the chair. Keep the same seated performance, body movement, hand gestures, head movement, mouth and lip movement, speaking timing, blocking, poses, screen placement, and two-handed grip. Change only the man, the handheld object, the green-screen setting and illumination, and the on-screen text.
Preserve every caption, subtitle, and other untargeted on-screen text element from @Video1 exactly as it appears, including its wording, styling, placement, animation, and timing, unless the user explicitly requests a specific text edit; text physically attached to a replaced target follows that replacement.
1. REPLACE the original man in the white t-shirt holding the microphone (0-6s) with MAN from @Image1 and @Image2. Put MAN into the shot matched beat-for-beat to the original speaking, direct gaze, head motion, lip motion, seated pose, and two-handed hold. Render MAN's swept-back gray hair, gray beard and mustache, mature face, very dark bottle-green open flannel over a white crew-neck T-shirt, left-wrist watch, and no bracelets consistently.
2. REPLACE the original black microphone with rectangular mic flag (0-6s) with FLASHLIGHT from @Image3, held in the same position and with the same two-handed grip, with its lens pointing upward toward MAN's face.
3. MODIFY only the solid green screen background and scene illumination (0-6s) so the room is completely pitch black with no green or room detail visible. At the opening, keep the flashlight off so MAN is barely visible as a silhouette; before the inherited speech begins, turn FLASHLIGHT on. Thereafter use only its upward light, matching UNDER-LIGHTING from @Image4: softly and clearly expose the chin, lips, nostrils, cheekbones, skin texture, gray beard, and identity; keep the eyes and forehead deeply shadowed. Do not overexpose the face or project light patterns or textures onto it. Keep shirt, T-shirt, and arms almost black, with only a faint glow on the hands near the flashlight.
4. REMOVE only all on-screen text and subtitles (1-3.5s and 3.6-6s) and reconstruct clean text-free footage beneath them consistently with the surrounding dark image.
Identity lock: MAN maps only to the man in the white t-shirt holding the microphone from 0-6s, with his complete image-defined identity and effective requested wardrobe locked across the shot; MAN is never duplicated onto another figure. Within 0-6s, replace the original source person identified as the man in the white t-shirt holding the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. FLASHLIGHT maps only to the original microphone and remains securely aligned with both hands. UNDER-LIGHTING applies only to the requested dark scene state.
Everything else — the inherited Spanish speech timing, seated pose, two-handed contact, and all non-text source content not changed above, the camera moves and all timing — stays exactly the same.
```

## Felipe 1.0 · Clips 2+4+5 — usado (luz favorita de Liz)

- job_id: `a48cc2d5-443c-4b3d-a47a-feb7856fbeb6`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 10 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`8e7a0d2d-671f-4c87-ab2d-5f184deac1c2` (media_input), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`ddc3da5e-3cd0-44f9-9157-8c86dd9ceb69` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261001_171617_a48cc2d5-443c-4b3d-a47a-feb7856fbeb6.mp4

```text
1) NO subtitles, NO captions, NO words, NO text of any kind anywhere on screen, in any frame.
2) This video has three shots joined by hard cuts: a side close-up (0 to 1.9 s), another side close-up (1.9 to 4.4 s) and a frontal close-up (4.4 s to the end). Keep the cuts exactly where they are and keep the exact framing of each shot: same camera angle, same distance, same crop, same head size and position. Do NOT zoom out, do NOT widen any shot, do NOT show his legs or a chair.
3) Keep body movement, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
4) Replace the microphone with the flashlight from reference image 3, held the same way, its lens pointing up toward his face. The flashlight is already ON from the very first frame to the last frame of the video, in all three shots. It never turns off and never turns on again.
5) Replace the man with the man from reference images 1 and 2: same face, gray hair and gray beard, very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, wristwatch on his left wrist, no bracelets. Same lip movements as the original man.
6) LIGHTING: the room is completely dark, pitch black, nothing of the room is visible, no green anywhere. The only light is the flashlight shining upward from below onto his face, with the same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. In the side shots the light falls on the side of his face that faces the flashlight. The light on his face is soft and well exposed, NOT blown out and NOT overexposed: his facial features, skin texture, gray beard and identity stay clearly readable, with no light patterns or textures projected on his face.
7) His body stays very dark: the shirt, the t-shirt and the arms are almost black, only his hands catch a faint glow near the flashlight. Only the face is clearly lit.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN (two complementary views): a middle-aged man with light skin, salt-and-pepper gray hair swept back with short sides, a neatly trimmed gray beard and mustache, and clearly defined natural facial features. Wardrobe: very dark bottle-green flannel button-down worn open over a white crew-neck T-shirt, left-wrist watch, no bracelets.
@Image3 — FLASHLIGHT, the replacement FLASHLIGHT: a black cylindrical handheld flashlight with a broad lens head, matte and knurled metal body.
@Image4 — UNDER-LIGHTING REFERENCE, the LIGHTING REFERENCE: a face isolated against blackness, softly illuminated upward from below with pronounced shadows over the eyes and forehead.
Video edit. Keep this @Video1 clip exactly as it is — the same three hard-cut shots (cuts at 1.9s and 4.4s), the same camera angles, distances, crops, head size and screen positions, the same seated blocking, hand gestures, body movement, head movement, mouth and lip movement, Spanish dialogue timing, pacing and timing of every shot. Change only the man, the handheld microphone, and the green-screen studio environment and lighting, keeping original blocking, poses, target motion, positions, screen placement and timing while rendering the replacement man’s complete image-defined appearance and stature.
1. REPLACE the original man in the white t-shirt (0-1.9s side close-up; 1.9-4.4s side close-up; 4.4-8.5s frontal close-up) with MAN from @Image1 and @Image2. Put MAN into every one of those shots, matched beat-for-beat to the original speaking, hand-held-object gestures, profile orientation, direct-to-camera gaze, and lip movements. Render MAN’s full declared appearance — light skin, swept-back gray hair, gray beard and mustache, very dark bottle-green open flannel shirt, white crew-neck T-shirt, and left-wrist watch. Keep his face and wardrobe consistent across all shots.
2. REPLACE the original black handheld microphone (0-8.5s across all three shots) with FLASHLIGHT from @Image3. Keep it firmly held in both hands at the original chest-height position, lens pointing upward toward MAN’s face; it is already switched on from the first frame through the final frame and never switches off or on again.
3. MODIFY only the green screen background and studio lighting (0-8.5s across all three shots) so the room is completely pitch black with no visible green or room detail. Use @Image4 only as the under-lighting reference: FLASHLIGHT is the sole light source, softly and clearly lighting MAN’s chin, lips, nostrils, cheekbones, skin texture, gray beard, and recognizable identity from below while leaving his eyes and forehead in dark horror-style shadow. Keep his shirt, T-shirt, and arms nearly black, with only faint hand glow near FLASHLIGHT; do not overexpose his face or project patterns or textures onto it.
Identity lock: MAN belongs only to the original man in the white t-shirt for 0-8.5s and is never duplicated onto another figure. Within the entire clip (0-8.5s), replace the original source person identified as the man in the white t-shirt in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person’s original appearance, subject only to other explicitly requested edits. Lock MAN’s complete image-defined identity and effective wardrobe across all cuts; retain the original two-handed contact with FLASHLIGHT. Do not render subtitles, captions, words, or text of any kind in any frame.
Everything else — the exact close-up framing, original hand positions, lip-sync timing, hard-cut structure, darkness outside the flashlight illumination, the camera moves and all timing — stays exactly the same.
```

## Felipe 1.0 · Clip 3 v2 — usado

- job_id: `62ebde8f-c6b8-4ef4-9118-dbd839195f5e`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 12 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`8e7a0d2d-671f-4c87-ab2d-5f184deac1c2` (media_input), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`c496770d-db79-476b-bac8-6683b7d8962d` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261001_202221_62ebde8f-c6b8-4ef4-9118-dbd839195f5e.mp4

```text
1) NO subtitles, NO captions, NO words, NO text of any kind anywhere on screen, in any frame.
2) FRAMING: keep exactly the same close frontal framing as the source video: same camera distance, same crop, same head size and position. Do NOT zoom out, do NOT widen the shot, do NOT show his legs or a chair.
3) BODY PROPORTIONS AND HAND HEIGHT (important): keep the man's body proportions exactly like the original man: same torso length, shoulders and chest in the same place in the frame. Do NOT make his torso longer. His hands stay at chest height, exactly as high as in the source for the whole video: the top of the flashlight is just below his chin, at about 44 percent of the frame height, and his clasped hands are at about 63 to 73 percent of the frame height. The hands must NOT drop to his stomach or waist.
4) Keep body movement, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
5) Replace the microphone with the flashlight from reference image 3, held the same way with both hands, its lens pointing up toward his face. The flashlight is already ON from the very first frame to the last frame of the video. It never turns off and never turns on again.
6) Replace the man with the man from reference images 1 and 2: same face, gray hair and gray beard, very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, wristwatch on his left wrist, no bracelets. Same lip movements as the original man.
7) LIGHTING: the room is completely dark, pitch black, nothing of the room is visible, no green anywhere. The only light is the flashlight shining upward from below onto his face, with the same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. The light on his face is soft, smooth and well exposed, NOT blown out and NOT overexposed: his facial features, skin texture, gray beard and identity stay clearly readable, with no light bands, light patterns or textures projected on his face or forehead.
8) His body stays very dark: the shirt, the white t-shirt and the arms are almost black, only his hands catch a faint glow near the flashlight. Only the face is clearly lit.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN (complementary views of the same man): middle-aged man with salt-and-pepper gray hair swept back, a neatly trimmed gray beard and mustache, light skin, average build, and a defined, natural-looking face. Wardrobe: very dark bottle-green flannel button-down shirt worn open over a white crew-neck T-shirt, dark trousers, and a wristwatch on his left wrist; no bracelets.
@Image3 — FLASHLIGHT, the replacement FLASHLIGHT: black handheld flashlight with a broad cylindrical lens housing, tapered neck, and textured knurled grip.
@Image4 — UNDER-LIGHTING, the LIGHTING REFERENCE: pitch-black surroundings and soft upward flashlight illumination that clearly reveals the face while casting dark shadows over the eyes and forehead.
Video edit. Keep this @Video1 clip exactly as it is — the same single 10.3-second shot, camera framing and composition, centered seated pose, close frontal crop, head size and position, camera distance, body proportions, torso, shoulders, chest placement, blocking, lip-sync timing, gestures, hand height, pacing and timing. Keep the original speaking performance, with the hands held at chest height: flashlight top just below the chin at about 44 percent of frame height and clasped hands at about 63 to 73 percent of frame height. Change only the man, microphone, green-screen setting, and illumination, keeping original poses, target motion, positions, screen placement and timing while rendering each replacement person's complete image-defined appearance and stature.
1. REPLACE the original man in the white t-shirt (0-10.3s, the full single shot) with MAN from @Image1 and @Image2. Put MAN into the shot matched beat-for-beat to the original downward glance, direct-to-camera speaking, head and brow movements, mouth and lip movements, upright seated pose, and two-handed chest-height grip. Render MAN's full declared appearance — swept-back gray hair, gray beard and mustache, light skin, natural average build, bottle-green open flannel shirt over a white crew-neck T-shirt, and left-wrist watch with no bracelets. Keep the face, beard, hair, wardrobe, and left-wrist watch consistent with MAN's declaration.
2. REPLACE the original black microphone with FLASHLIGHT from @Image3 (0-10.3s, the full single shot). Keep it gripped by both hands at the original chest-height position, with its lens pointing upward toward MAN's face; the flashlight is already continuously on from the first frame through the last frame, with no switching event.
3. MODIFY only the solid green screen background and studio illumination (0-10.3s, the full single shot) so the surroundings are completely pitch black with no visible room or green spill, guided by UNDER-LIGHTING from @Image4. The flashlight is the only light: cast soft, smooth, well-exposed upward light on MAN's chin, lips, nostrils, cheekbones, skin texture, gray beard, and identifiable face, with dark shadows over his eyes and forehead. Keep his shirt, white T-shirt, arms, and body almost black, with only a faint glow on his hands near the flashlight; do not project bands, patterns, or textures onto his face or forehead.
Identity lock: MAN belongs only to the original man in the white t-shirt from 0-10.3s and is never duplicated onto another figure. Within 0-10.3s, replace the original source person identified as the man in the white t-shirt in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity and effective wardrobe only within 0-10.3s. Protect the two-hand flashlight grip, chest-height hand placement, flashlight orientation, and continuous beam. Do not show legs, chair, room details, green background, captions, subtitles, words, or text of any kind in any frame.
Everything else — the original close frontal framing, centered screen placement, seated posture, speaking performance, exact body proportions, hand gestures, head movement, mouth movement, flashlight contact, the camera moves and all timing — stays exactly the same.
```

## Felipe 1.0 · Clips 6+7 — usado

- job_id: `1bf12125-adf8-4f4b-9f0b-f4a30ce98fac`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 9 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`8e7a0d2d-671f-4c87-ab2d-5f184deac1c2` (media_input), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`62f06453-b9a9-4ec2-ac6e-1aa6937f4e92` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261001_180400_1bf12125-adf8-4f4b-9f0b-f4a30ce98fac.mp4

```text
1) NO subtitles, NO captions, NO words, NO text of any kind anywhere on screen, in any frame.
2) This video has two shots joined by a hard cut at 2.87 s. SHOT A (0 to 2.87 s): a close-up detail shot of his hands holding the object, seen from the side. SHOT B (2.87 s to the end): a frontal close shot of the man talking, with a slow camera pull-back (zoom out) exactly like the source. Keep the cut where it is, keep the exact framing of each shot and copy the camera movement of shot B exactly. Do NOT zoom out shot A, do NOT widen any shot more than the source does.
3) BODY PROPORTIONS AND HAND HEIGHT (important): keep the man's body proportions exactly like the original man: same torso length, shoulders and chest in the same place in the frame. Do NOT make his torso longer. In shot B his hands stay at chest height, exactly as high as in the source: the top of the flashlight is just below his chin, and his clasped hands are at about 66 to 72 percent of the frame height at the start of shot B and about 62 to 68 percent at the end. The hands must NOT drop to his stomach or waist.
4) Keep body movement, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
5) Replace the microphone with the flashlight from reference image 3, held the same way, its lens pointing up toward his face.
6) Replace the man with the man from reference images 1 and 2: same face, gray hair and gray beard, very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, wristwatch on his left wrist, no bracelets. In shot A his hands and wrists must match this man. Same lip movements as the original man.
7) FLASHLIGHT ON AND OFF: the flashlight is ON from the first frame. In shot A it is on the whole time. In shot B it stays on while he talks; at 7.4 seconds (right after he finishes speaking) he switches the flashlight OFF and the whole image goes completely black until the end of the video. Nothing visible after it turns off.
8) LIGHTING while the flashlight is on: the room is completely dark, pitch black, nothing of the room is visible, no green anywhere. The only light is the flashlight. In shot A the light comes from the flashlight lens and gently lights his hands. In shot B it shines upward from below onto his face, with the same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead; soft, smooth and well exposed, NOT blown out, no light bands or patterns on his face; his features, gray beard and identity clearly readable.
9) His body stays very dark: the shirt, the white t-shirt and the arms are almost black, only his hands catch a faint glow near the flashlight.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN (complementary full-body and face views): photogenic middle-aged man with light skin, salt-and-pepper gray hair swept back, gray beard and mustache, defined brows, warm brown eyes, and an average, natural build. Wardrobe: very dark bottle-green flannel button-down worn open over a white crew-neck T-shirt, dark trousers, and a wristwatch on the left wrist; no bracelets.
@Image3 — FLASHLIGHT, the replacement FLASHLIGHT: black handheld flashlight with a wide cylindrical lens housing, ribbed metal grip, and rear push-button.
@Image4 — LIGHTING REFERENCE, the LIGHTING: soft horror-style upward flashlight illumination, clearly exposing the chin, lips, nostrils, cheekbones, gray beard, and facial identity while leaving the eyes and forehead in soft shadow.
Video edit. Keep this @Video1 clip exactly as it is — the same two shots and hard cut at 2.87s, the exact framing of each shot, the same slow pull-back in shot B only, the same blocking, body proportions, torso length, shoulder and chest placement, poses, hand gestures, head movement, mouth movement, lip-sync, pacing and timing. Change only the man, microphone, darkness and explicitly targeted subtitles, keeping the original chest-height hand placement and inherited performance.
Preserve every caption, subtitle, and other untargeted on-screen text element from @Video1 exactly as it appears, including its wording, styling, placement, animation, and timing, unless the user explicitly requests a specific text edit; text physically attached to a replaced target follows that replacement.
1. REPLACE the original man holding the microphone (shot A 0-2.87s; shot B 2.87s-7.4s) with MAN from @Image1 and @Image2. Put MAN into both shots, matched beat-for-beat to the original hand grip, speaking, facial articulation, gaze, and pose. Render his gray swept-back hair, gray beard, recognizable face, very dark bottle-green open flannel over the white T-shirt, left-wrist watch, and no bracelets. Keep his source-matched body proportions exactly: in shot B, his hands remain at chest height, the flashlight top just below his chin, never lowered toward his stomach or waist.
2. REPLACE the original black handheld microphone (shot A 0-2.87s; shot B 2.87s-7.4s) with FLASHLIGHT from @Image3, held vertically in the identical two-hand grip with its lens aimed upward toward MAN's face. It is switched on from the first frame through 7.4s; preserve all finger contact and occlusion naturally.
3. MODIFY only the green-screen setting and illumination (shot A 0-2.87s; shot B 2.87s-7.4s) so the room is completely pitch black with no green or room detail visible. The flashlight is the only light: in shot A it gently lights MAN's hands; in shot B it gives the soft, smooth, well-exposed upward horror lighting from @Image4, with no blown highlights, bands, or patterns. Keep his shirt, white T-shirt, and arms almost black, with only faint hand glow near the flashlight.
4. REMOVE only all reported subtitle overlays, including “Lo que da miedo” and “es dejar pasar oportunidades.”, so no captions, words, or text appear in any frame.
5. MODIFY only the flashlight state from 7.4s to the end: MAN switches FLASHLIGHT off immediately after speaking, and the entire image becomes completely black with nothing visible.
Identity lock: MAN maps only to the original man holding the microphone from 0-7.4s and is never duplicated onto another figure. Within 0-7.4s, replace the original source person identified as the man holding the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity and effective wardrobe, with the requested no-bracelets constraint, across both shots. Protect the flashlight's hand contact and keep its lens below his chin in shot B.
Everything else — the original shot structure, framing, body and hand placement, performance beats, darkness after 7.4s, the camera moves and all timing — stays exactly the same.
```

## Felipe 1.0 · Toma final showroom (clip 8) — usado

- job_id: `135de18e-058c-4ac9-b3d3-b004d6daae1a`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 11 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`8e7a0d2d-671f-4c87-ab2d-5f184deac1c2` (media_input), 4=image:`97bc0ebe-44c3-42f3-aed1-17cb986183e6` (media_input), 5=image:`ebff942c-83c5-413a-9484-4a7d969af75f` (media_input), 6=image:`1f823f09-4d4a-478d-9976-abddb7149d39` (media_input), 7=video:`4fe4597f-a7bc-4e80-95fc-efd67aaf8bb8` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261001_005246_135de18e-058c-4ac9-b3d3-b004d6daae1a.mp4

```text
Keep the camera movement (a smooth continuous pull-back with no cuts or jumps), framing, body movement, the action of standing up, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video. Make these replacements:
1) Replace the microphone with the flashlight from reference image 3 (switched off), in every frame. He holds it and sets it down exactly the same way.
2) Replace the man with the man from reference images 1 and 2: same face, gray hair and gray beard, very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, pure black cargo pants (black, not brown), black leather sneakers, wristwatch on his left wrist, no bracelets. Same lip movements as the original man.
3) Replace the black box he sits on with the walnut armchair with gray cushion from reference image 4; he stands up from this armchair.
4) Replace the tall wooden stool with the tall round table from reference image 5: walnut round top, single black column, round black base, same position. The flashlight rests on its top.
5) Replace the whole green screen studio with the showroom interior from reference image 6: warm brown plaster walls, curved ceiling with recessed square spotlights and a large round ceiling cove, floor-to-ceiling windows with sheer white curtains, green plants in white pots, polished gray concrete floor with thin dark curved inlaid lines. As the camera pulls back, more of the showroom and its ceiling spotlights are revealed. No green anywhere. Remove the white chair at the bottom-left corner of the frame; show the concrete floor there.
6) Lighting: normal, warm and natural like reference image 6, daylight from the windows plus ceiling spotlights. Not dark, not horror.
7) NO subtitles, NO captions, NO text of any kind on screen.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN: photogenic light-skinned adult man with salt-and-pepper gray hair swept back, neatly trimmed gray beard and mustache, defined brows, natural facial lines, and an average build. Wardrobe: very dark bottle-green flannel button-down worn open over a white crew-neck T-shirt, pure black cargo pants, black leather sneakers, and a wristwatch on his left wrist; no bracelets.
@Image3 — FLASHLIGHT, the replacement FLASHLIGHT: black cylindrical handheld flashlight with a broad head, textured grip, and unlit lens.
@Image4 — ARMCHAIR, the replacement ARMCHAIR: walnut wood armchair with angular arms and frame, a dark gray button-tufted seat cushion, and gray upholstered back cushion.
@Image5 — TABLE, the replacement TABLE: tall round walnut tabletop on a single black column with a round black base.
@Image6 — SHOWROOM, the replacement LOCATION: warm brown plaster interior with a curved ceiling, recessed square spotlights, a large circular ceiling cove, floor-to-ceiling windows with sheer white curtains, green plants in white pots, and polished gray concrete flooring with thin dark curved inlaid lines.
Video edit. Keep this @Video1 clip exactly as it is — the same single continuous 0-9.6s take, smooth pull-back, framing and composition, standing action, hand gestures, head movement, speech timing and lip movement, blocking, positions, and timing of every shot. Change only the man, microphone, equipment case, stool, green-screen studio, and any on-screen text, while rendering the replacement man's complete image-defined appearance and stature; only the requested replacements alter the set.
1. REPLACE the original man in the white t-shirt (0-9.6s) with MAN from @Image1 and @Image2. Put MAN into the full take, matched beat-for-beat to the original rising from the armchair, setting down the flashlight, speaking to camera, and gesturing. Render MAN's swept-back gray hair, gray beard and mustache, light skin, very dark bottle-green open flannel over a white T-shirt, pure black cargo pants, black leather sneakers, left-wrist watch, and no bracelets consistently.
2. REPLACE the original handheld microphone (0-9.6s) with FLASHLIGHT from @Image3, switched off. The man holds it and sets it onto the table at the identical moments and contact points.
3. REPLACE the original black equipment case (0-9.6s) with ARMCHAIR from @Image4. The man begins seated on it and rises with the inherited timing and contact.
4. REPLACE the original barstool (0-9.6s) with TABLE from @Image5 in the identical position. The flashlight rests on its walnut top after it is set down.
5. REPLACE the original green screen cyclorama room (0-9.6s) with SHOWROOM from @Image6. Reveal more of the showroom and ceiling spotlights naturally as the camera pulls back; use warm natural daylight from the windows plus ceiling spotlights, with no green anywhere.
6. REMOVE only the white chair at the bottom-left corner (0-9.6s) and reconstruct the revealed area as polished concrete floor.
7. REMOVE only any on-screen subtitles, captions, and text of any kind (0-9.6s), leaving clean underlying footage.
Identity lock: MAN maps only to the man in the white t-shirt from 0-9.6s and is never duplicated onto another figure. Within 0-9.6s, replace the original source person identified as the man in the white t-shirt in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity and effective wardrobe throughout 0-9.6s; retain his left-wrist watch and no bracelets. FLASHLIGHT, ARMCHAIR, TABLE, and SHOWROOM remain locked to their mapped replacements; preserve all hand, seating, floor-contact, and flashlight-on-table contacts. The man's soft floor shadow follows MAN, ARMCHAIR, TABLE, and SHOWROOM within the active window.
Everything else — the inherited Spanish speech audio, performance sync, source action beats, camera moves and all timing — stays exactly the same.
```

## Felipe 1.0 · Prueba 720p con chroma

- job_id: `2018c235-eca4-420c-8ccf-9fca91a05b92`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 6 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`97bc0ebe-44c3-42f3-aed1-17cb986183e6` (media_input), 4=video:`e553fa7a-b601-4412-9372-5a9f733f5f6b` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20260930_221614_2018c235-eca4-420c-8ccf-9fca91a05b92.mp4

```text
Replace three things in the video and keep everything else (camera, framing, green screen background, body movement, hand gestures, head movement, mouth and lip movement while talking, timing) exactly the same:
1) Replace the man in the white t-shirt with the gray-haired, gray-bearded man from the first two reference images: same face, gray hair and beard, wearing a very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, black cargo pants, black leather sneakers, a wristwatch on his left wrist, no bracelets. He talks with the same lip movements as the original man.
2) Replace the black handheld microphone in his hands with a small black metal handheld flashlight, held the same way with both hands, lens pointing up.
3) Replace the white plastic chair he sits on with the mid-century walnut wood armchair with gray upholstered cushion from the third reference image.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN (complementary views of the same man): gray-haired, gray-bearded adult man with light-to-medium skin, a neatly swept-back salt-and-pepper hairstyle, full trimmed gray beard and mustache, defined brows, and a natural photogenic appearance. Wardrobe: very dark bottle-green flannel button-down shirt worn open over a white crew-neck T-shirt, black cargo pants, black leather sneakers, a wristwatch on his left wrist, no bracelets.
@Image3 — ARMCHAIR, the replacement ARMCHAIR: mid-century walnut wood armchair with angled wooden arms and legs, a gray upholstered seat cushion, and a gray upholstered backrest.
Video edit. Keep this @Video1 clip exactly as it is — the same single 4.0-second shot, camera framing and composition, green screen backdrop, Spanish speech, original body movement, hand gestures, head movement, mouth and lip movement, seated blocking, lighting, pacing and timing. Change only the seated man, the handheld microphone, and the white chair, keeping original positions, screen placement and timing while rendering the replacement man's complete image-defined appearance and stature.
Preserve every caption, subtitle, and other untargeted on-screen text element from @Video1 exactly as it appears, including its wording, styling, placement, animation, and timing, unless the user explicitly requests a specific text edit; text physically attached to a replaced target follows that replacement.
1. REPLACE the original seated man holding the microphone (0.0-4.0s, the full shot) with MAN from @Image1 and @Image2. Put MAN into the full shot, matched beat-for-beat to the original speaking performance, direct gaze, seated posture, hand gestures, head motion, and lip movements. Render MAN's full declared appearance — swept-back salt-and-pepper hair, trimmed gray beard and mustache, light-to-medium skin, very dark bottle-green open flannel shirt over a white crew-neck T-shirt, black cargo pants, black leather sneakers, left-wrist watch, and no bracelets. Keep his face, hair, beard, and outfit consistent with MAN's declaration throughout.
2. REPLACE the original white chair with metal legs (0.0-4.0s, the full shot) with ARMCHAIR from @Image3, preserving the seated contact, lower-center placement, and natural occlusion by the man.
3. REPLACE the original black microphone with rectangular flag (0.0-4.0s, the full shot) with a small black metal handheld flashlight, held the same way with both hands at chest level, with its lens pointing upward, preserving its contact and motion timing.
Identity lock: MAN belongs only to the seated man holding the microphone for 0.0-4.0s and is never duplicated onto another figure. Within 0.0-4.0s, replace the original source person identified as the seated man holding the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity, effective wardrobe, gray hair and beard, and left-wrist watch across the shot. Preserve his two-handed grip on the flashlight and his seated contact with ARMCHAIR; the chair's shadows and occlusions resolve naturally on the green floor.
Everything else — the green screen background, dynamic Spanish subtitles, and all untargeted elements, the camera moves and all timing — stays exactly the same.
```

## Felipe 1.0 · Prueba 480p iluminado

- job_id: `48255752-93a6-4ea4-b707-83a2b18a4bb4`
- modelo: `hf_mult_replace_object` · resolución: 480p · duración: 6 · aspecto: auto
- medias: 1=image:`4c9a53dc-1068-409e-80df-156d193549f1` (image_job), 2=image:`feb10921-0f4b-44a1-9f70-03134c3520d0` (media_input), 3=image:`97bc0ebe-44c3-42f3-aed1-17cb986183e6` (media_input), 4=video:`e553fa7a-b601-4412-9372-5a9f733f5f6b` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20260930_223542_48255752-93a6-4ea4-b707-83a2b18a4bb4.mp4

```text
Keep the camera, framing, body movement, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video. Make these changes:
1) Replace the man in the white t-shirt with the gray-haired, gray-bearded man from the first two reference images: same face, gray hair and beard, very dark bottle-green flannel button-down shirt worn open over a white crew-neck t-shirt, BLACK cargo pants (pure black, not brown), black leather sneakers, a wristwatch on his left wrist, no bracelets. He talks with the same lip movements as the original man.
2) Replace the black handheld microphone in his hands with a small black metal handheld flashlight, switched ON, held the same way with both hands, lens pointing up toward his face.
3) Replace the white plastic chair with the mid-century walnut wood armchair with gray upholstered cushion from the third reference image.
4) LIGHTING: horror / suspense mood. The room is completely dark, pitch black background, no green screen visible at all. The ONLY light comes from the flashlight in his hands, shining upward from below onto his face: classic horror under-lighting, bright underside of chin, nose and cheekbones, deep shadows above the eyes and on the forehead. The light falls off quickly: his face is clearly lit, his shoulders and upper chest dimly lit, his hands and forearms catch some light, his legs and the armchair fade into near darkness. Cool white light, cinematic, subtle film grain.
5) NO subtitles, NO captions, NO text of any kind on screen.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image2 — MAN, the replacement MAN (complementary views of the same man): gray hair swept back, neatly trimmed gray beard and mustache, light-to-medium skin, natural adult male face and features, medium build. Wardrobe: very dark bottle-green flannel button-down worn open over a white crew-neck T-shirt, pure black cargo pants, black leather sneakers, and a wristwatch on his left wrist; no bracelets.
@Image3 — ARMCHAIR, the replacement ARMCHAIR: mid-century walnut wood armchair with angular wooden arms and legs, gray upholstered seat cushion and gray upholstered backrest.
Video edit. Keep this @Video1 clip exactly as it is — the same single 4.7-second take, camera framing and composition, camera moves, pacing and timing, Spanish dialogue, seated blocking, hand gestures, head movement, mouth and lip movement, and the original speaker's performance. Change only the man, handheld object, chair, green-screen setting and lighting, and subtitles; retain the original screen positions, contact points, and timing while rendering the replacement man's complete image-defined appearance and stature.
Preserve every caption, subtitle, and other untargeted on-screen text element from @Video1 exactly as it appears, including its wording, styling, placement, animation, and timing, unless the user explicitly requests a specific text edit; text physically attached to a replaced target follows that replacement.
1. REPLACE the original man in the white t-shirt (0-4.7s, centered seated speaker) with MAN from @Image1 and @Image2. Put MAN into the full take, matched beat-for-beat to the original talking, forward gaze, seated pose, two-handed grip, and lip movements. Render MAN's gray swept-back hair, gray beard and mustache, natural facial features, very dark bottle-green open flannel over a white crew-neck T-shirt, pure black cargo pants, left-wrist watch, and no bracelets consistently.
2. REPLACE the original white chair (0-4.7s, beneath and behind the seated speaker) with ARMCHAIR from @Image3, preserving the original seated contact, placement, occlusion, and timing. Keep its walnut wood frame and gray upholstered cushion consistent with ARMCHAIR's declaration.
3. REPLACE the original black handheld microphone (0-4.7s, held at chest level) with a small black metal handheld flashlight, switched on, held in the same two-handed grip with its lens pointing upward toward the man's face; preserve the original hand placement, interaction, and timing.
4. REPLACE the green screen background and floor (0-4.7s) with a completely dark, pitch-black room with no green screen visible. Make the flashlight the only light source: cool-white cinematic under-lighting from below, brightly illuminating the underside of the chin, nose, and cheekbones, with deep shadows above the eyes and across the forehead; let light fall off rapidly so the face is clear, shoulders and upper chest dim, hands and forearms partly lit, and legs and ARMCHAIR nearly disappear into darkness. Add subtle film grain only.
5. REMOVE only the on-screen subtitles (0.8-4.7s) and reconstruct clean footage beneath them consistently with the surrounding image.
Identity lock: MAN maps only to the man in the white t-shirt during 0-4.7s, with his complete image-defined identity and requested effective wardrobe locked across the take. Within 0-4.7s, replace the original source person identified as the man in the white t-shirt in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. MAN is never duplicated onto another figure. Keep the flashlight securely aligned to both hands and its upward beam, and preserve the seated contact with ARMCHAIR.
Everything else — the source dialogue, performance timing, original hand and head motion, and the camera moves and all timing — stays exactly the same.
```
