# Prompts Genjutsu — Felipe Juarez 2.0

Texto exacto enviado a Higgsfield, recuperado del historial de generaciones (5 oct 2026). En `medias` el orden = número de "reference image N" del prompt.

## Felipe 2.0 · Clips 2+4+6

- job_id: `d2894c4a-9fe2-4aab-85e6-68ae784999f4`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 6 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`55b33da9-f6a8-4189-b2b4-3144a6b22ca9` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261002_225308_d2894c4a-9fe2-4aab-85e6-68ae784999f4.mp4

```text
1) NO subtitles, NO captions, NO words, NO text of any kind anywhere on screen, in any frame.
2) This video has three shots joined by hard cuts: a side close-up (0 to 1.9 s), another side close-up (1.9 to 4.4 s) and a close-up detail of his hand holding the object (4.4 s to the end). Keep the cuts exactly where they are and keep the exact framing of each shot: same camera angle, same distance, same crop, same head and hand size and position. Do NOT zoom out, do NOT widen any shot.
3) Keep body movement, hand gestures, finger movement, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
4) Replace the microphone with the flashlight from reference images 2 and 3, held the same way, its lens pointing up toward his face. The flashlight is already ON from the very first frame to the last frame, in all three shots. It never turns off and never turns on again.
5) Replace the man with the man from reference image 1 ONLY, faithfully keeping his exact identity: a man in his early thirties with short almost-black hair, thick dark eyebrows, dark brown eyes and a full, neatly trimmed dark beard. NO gray hair, NO gray beard, do not age him. Dark forest green button-down shirt worn open over a white crew-neck t-shirt; in the hand close-up the visible pants are black cargo pants, pure black, not blue, not brown. Wristwatch with a brown leather strap on his left wrist only; no watch on the other wrist; no bracelets. NO rings on any finger: remove the ring, all fingers are bare. Same lip movements as the original man.
6) LIGHTING: the room is completely dark, pitch black, nothing of the room is visible, no green anywhere. The only light is the flashlight shining upward from below onto his face, with the same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. In the side shots the light falls on the side of his face that faces the flashlight. The light on his face is soft and well exposed, NOT blown out and NOT overexposed: his facial features, skin texture, dark beard and identity stay clearly readable, with no light patterns or textures projected on his face.
7) His body stays very dark: the shirt, the t-shirt, the arms and the pants are almost black, only his hands catch a faint glow near the flashlight. Only the face is clearly lit.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN, the replacement MAN: early-thirties man with short almost-black hair, thick dark eyebrows, dark brown eyes, light-to-medium skin, and a full neatly trimmed dark beard. Wardrobe: dark forest-green button-down shirt worn open over a white crew-neck T-shirt, pure black cargo pants, and a brown leather-strap wristwatch on the left wrist only; bare fingers, no rings, bracelets, or other wristwear.
@Image2 and @Image3 — FLASHLIGHT, the replacement FLASHLIGHT: black cylindrical handheld flashlight with a flared lens housing, reflective lens, and textured knurled grip.
@Image4 — UNDERLIGHTING, the LIGHTING REFERENCE: pitch-black room with soft, readable upward flashlight illumination on the face, lighting the chin, lips, nostrils, and cheekbones while leaving the eyes and forehead in deep shadow.
Video edit. Keep this @Video1 clip exactly as it is — the same three shots and hard cuts at 1.9s and 4.4s, the same camera moves, framing, composition, crop, subject scale and screen placement, the same seated blocking, body movement, hand gestures, finger movement, head movement, mouth and lip movement, speech timing, chair, pacing and timing of every shot. Change only the man, microphone, background, lighting, and any on-screen text, keeping original poses, target motion, positions and timing while rendering the replacement man's complete image-defined appearance and stature.
1. REPLACE the original man in the white shirt (0-1.9s side close-up; 1.9-4.4s side close-up; 4.4-5.3s hand detail) with MAN from @Image1. Put MAN into every one of those shots, matched beat-for-beat to the original speaking, seated posture, grip, finger adjustment, and lip movements. Render MAN's short almost-black hair, thick dark eyebrows, dark brown eyes, neatly trimmed dark beard, forest-green open shirt over a white T-shirt, black cargo pants in the hand shot, and brown leather-strap left-wrist watch only; all fingers are bare.
2. REPLACE the black microphone with square flag (0-1.9s; 1.9-4.4s; 4.4-5.3s) with FLASHLIGHT from @Image2 and @Image3. Keep it held in exactly the original hands and contact positions, vertically oriented with its lens aimed upward toward MAN's face; it is already continuously switched on from the first frame through the last frame.
3. MODIFY only the green-screen background and scene illumination (0-5.3s) so the room is completely pitch black with no visible green or room detail, using UNDERLIGHTING from @Image4: the flashlight is the sole light source, softly underlighting MAN's face from below without overexposure, projection patterns, or texture. Keep his face, skin texture, beard, and identity clearly readable; keep his shirt, T-shirt, arms, and pants nearly black, with only faint hand glow near the flashlight.
4. REMOVE only any subtitles, captions, words, labels, or other on-screen text (0-5.3s) and reconstruct each revealed area consistently from the immediately surrounding darkness, with all former occlusions resolving naturally.
Identity lock: MAN belongs only to the original man in the white shirt for 0-5.3s and is never duplicated onto another figure. Within the entire clip, replace the original source person identified as the man in the white shirt in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete @Image1 identity, effective wardrobe, bare fingers, left-wrist-only brown leather watch, and no bracelets across all shots. Lock FLASHLIGHT to the original microphone's hand contact and its continuously on upward beam. Apply @Image4 underlighting only within the entire clip; no green screen, room detail, text, ring, or original microphone may remain.
Everything else — the seated blocking, hand contact, finger articulation, lip-sync performance, shot framing and crop, the camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clips 1+5+7 (5 y 7 fallaron)

- job_id: `bb8cdb43-e347-4451-aa7b-7b1c00c7b930`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 15 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`7ef51939-8896-40c8-bc12-e28f9e304f73` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261002_231418_bb8cdb43-e347-4451-aa7b-7b1c00c7b930.mp4

```text
1) NO subtitles, NO captions, NO words, NO text of any kind anywhere on screen, in any frame.
2) This video has three frontal close-up shots joined by hard cuts: shot A (0 to 6.5 s), shot B (6.5 to 10.8 s) and shot C (10.8 s to the end). Keep the cuts exactly where they are and keep the exact framing of each shot: same camera distance, same crop, same head size and position, his head near the top and his hands with the object at the bottom center. Do NOT zoom out, do NOT widen any shot, do NOT show his legs or a chair.
3) Keep body movement, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video. His hands stay at the same height as in the source, between 72% and 85% of the frame height from the top, in every shot — hands must NOT drop to the stomach.
4) Replace the microphone with the flashlight from reference images 2 and 3, held the same way with both hands, its lens pointing up toward his face.
5) Replace the man with the man from reference image 1 ONLY, faithfully keeping his exact identity in all three shots: a man in his early thirties with short almost-black hair, thick dark eyebrows, dark brown eyes and a full, neatly trimmed dark beard. Dark forest green button-down shirt worn open over a white crew-neck t-shirt. Wristwatch with a brown leather strap on his left wrist, which appears on the RIGHT side of the screen; no watch on the other wrist; no bracelets. Same lip movements as the original man.
6) FLASHLIGHT TIMING: shot A starts in darkness with the flashlight OFF: his silhouette is only barely visible in the dark. Then, before he starts talking, he switches the flashlight ON and the light visibly comes on and reveals his face. From that moment the flashlight stays ON until the very last frame of the video: it is already ON for all of shot B and all of shot C, and it never turns off again.
7) LIGHTING: the room is completely dark, pitch black, nothing of the room is visible, no green anywhere. The ONLY light source is the flashlight shining upward from below onto his face — no key light, no fill light, no side light, no studio light — with the same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. The light on his face is soft and well exposed, NOT blown out and NOT overexposed: his facial features, skin texture, dark beard and identity stay clearly readable, with no light patterns or textures projected on his face.
8) His body stays very dark: the shirt, the t-shirt and the arms are almost black, only his hands catch a faint glow near the flashlight. Only the face is clearly lit.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN, the replacement MAN: early-thirties man with short almost-black hair, thick dark eyebrows, dark brown eyes, and a full neatly trimmed dark beard. Wardrobe: dark forest-green button-down worn open over a white crew-neck T-shirt; brown-leather-strap wristwatch on his left wrist only, no bracelets.
@Image2 and @Image3 — FLASHLIGHT, the replacement FLASHLIGHT: black handheld flashlight with a wide circular lens housing, reflective lens, and textured black grip.
@Image4 — UNDERLIGHT, the LIGHTING REFERENCE: soft, well-exposed upward flashlight illumination on the chin, lips, nostrils, and cheekbones, with deep shadow over the eyes and forehead against pitch black.
Video edit. Keep this @Video1 clip exactly as it is — the same three frontal close-up shots and hard cuts at 6.5s and 10.8s, the same camera distance, crop, head size and near-top head placement, the same hands and held object at bottom center between 72% and 85% of frame height, the same body movement, gestures, head movement, Spanish speech, mouth and lip timing, pacing and timing. Change only the man, microphone, background, lighting, and any on-screen text; do not widen, zoom out, or reveal legs or a chair.
1. REPLACE the original man in the white shirt speaking (shot A 0-6.5s, shot B 6.5-10.8s, shot C 10.8-13s) with MAN from @Image1. Put MAN into every one of those shots, matched beat-for-beat to the original seated direct-to-camera delivery and two-handed held-object posture. Render MAN's full declared appearance — short almost-black hair, thick dark eyebrows, dark brown eyes, neatly trimmed full dark beard, forest-green open shirt over white T-shirt, and left-wrist brown leather watch on the right side of the screen. Keep his face and wardrobe consistent across all shots.
2. REPLACE the original black microphone with FLASHLIGHT from @Image2 and @Image3 (shot A 0-6.5s, shot B 6.5-10.8s, shot C 10.8-13s). Keep it held in both hands at the original height, with its lens pointing upward toward MAN's face. In shot A, begin with the flashlight off and MAN barely visible as a silhouette, then before he begins talking switch it on visibly; keep it on continuously from that moment through 13s, including all of shots B and C.
3. MODIFY only the green screen backdrop and source lighting (shot A 0-6.5s, shot B 6.5-10.8s, shot C 10.8-13s) so the room is completely pitch black with no green or visible room detail. Use only FLASHLIGHT's upward illumination, matching UNDERLIGHT from @Image4: softly expose MAN's facial features, skin texture, and beard without blowout or projected patterns; leave his shirt, T-shirt, and arms almost black, with only faint hand glow near the flashlight.
4. REMOVE only any on-screen subtitles, captions, words, or text of any kind (0-13s) and reconstruct each revealed area consistently from the immediately surrounding background, with all former occlusions resolving naturally.
Identity lock: MAN belongs only to the original man in the white shirt speaking for 0-13s and is never duplicated onto another figure. Within 0-13s, replace the original source person identified as the man in the white shirt speaking in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity, wardrobe, left-wrist watch placement, and no-bracelet appearance across all shots. Protect the two-handed flashlight contact and its upward lens orientation. FLASHLIGHT remains the sole light source after activation.
Everything else — the exact close-up framing, original speaking performance, hand height, lip sync, hard-cut timing, camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clip 1 intento 1 (tiempos en segundos; encendido tarde 4.42 s)

- job_id: `7898f5f3-bf05-4d18-9f72-136a6a1303d3`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 7 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`4513e4ed-ba6d-4132-9e23-e5a05017bb1e` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_162653_7898f5f3-bf05-4d18-9f72-136a6a1303d3.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. Keep exactly the same close framing, do NOT zoom out. Keep his exact pose, hand position and lip movement.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; dark green shirt open over a white t-shirt. Brown leather watch on the right side of the screen only.
4. Replace the microphone with the flashlight from reference image 2.
5. FLASHLIGHT SWITCH-ON - exact timing, this is the key moment of the shot:
- 0.00 s to 0.45 s: the room is almost pitch black and the flashlight is OFF. Only a faint silhouette of his head and shoulders is barely visible. No light on his face at all.
- At 0.45 s his right thumb clearly presses the button on the flashlight with a small, visible click movement.
- The light turns ON INSTANTLY in a single frame, like a real flashlight, NOT a slow fade-in. The lens glows bright at that same frame.
- From 0.50 s to the end the flashlight stays ON and never flickers, never dims, never turns off.
- He starts talking only after the light is on.
6. Lighting once ON: same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. Soft and well exposed, NOT blown out, no patches or blotches on the skin, no light patterns projected on his face. The flashlight is the ONLY light source: no key, fill or side light. Black room, body very dark, only his hands catch a faint glow.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN, the replacement MAN: early-thirties man with short almost-black hair, thick eyebrows, dark brown eyes, a full neatly trimmed dark beard, and a natural medium build. Wardrobe: dark green open button-up shirt over a white T-shirt, dark trousers; brown leather watch on the wrist at the right side of the screen only.
@Image2 and @Image3 — FLASHLIGHT, the replacement FLASHLIGHT: compact black handheld flashlight with a wide round lens housing, reflective lens, and textured cylindrical grip.
@Image4 — UNDER-LIGHTING REFERENCE, the LIGHTING REFERENCE: near-black room with a flashlight held below the face, creating soft dramatic upward illumination on the chin, lips, nostrils, and cheekbones while the eyes and forehead remain shadowed.
Video edit. Keep this @Video1 clip exactly as it is — the same single 6.7-second close framing, static camera, centered seated performance, pose, two-handed grip position, screen placement, pacing and timing. Change only the man, microphone, green-screen setting, lighting, and requested flashlight-switch moment, keeping original blocking, positions, and target motion while rendering the replacement man's complete image-defined appearance and stature.
1. REPLACE the original man in the white T-shirt holding the microphone (0.00-6.7s) with MAN from @Image1. Put MAN into the entire shot, matched beat-for-beat to the original seated forward-facing performance, pose, hand position, and lip movement after the flashlight turns on. Render MAN's short almost-black hair, thick eyebrows, dark brown eyes, full trimmed beard, dark green open shirt over a white T-shirt, and brown leather watch only on the screen-right wrist. Keep his face and wardrobe consistent throughout.
2. REPLACE the original black microphone with FLASHLIGHT from @Image2 and @Image3 (0.00-6.7s). Keep it held naturally in the same two-handed lower-center position. From 0.00-0.45s it is off. At 0.45s, show MAN's right thumb make a small clear button-click movement; the flashlight turns on instantly in that single frame, with its lens glowing immediately. From 0.50-6.7s it remains continuously on without flicker, dimming, or switching off.
3. MODIFY only the green screen backdrop and studio illumination (0.00-6.7s) so that the setting is a black room. From 0.00-0.45s, make it almost pitch black: only a faint head-and-shoulders silhouette is visible, with no light on the face. From 0.50-6.7s, use FLASHLIGHT as the only light source, matching @Image4: soft, well-exposed upward light on the chin, lips, nostrils, and cheekbones; dark shadow over the eyes and forehead; very dark body and black surroundings; faint glow only on the hands. Do not create blown highlights, skin blotches, projected face patterns, key light, fill light, or side light. MAN begins speaking only after the flashlight is on.
Identity lock: MAN from @Image1 belongs only to the original man in the white T-shirt holding the microphone during 0.00-6.7s and is never duplicated onto another figure. Within 0.00-6.7s, replace the original source person identified as the man in the white t-shirt holding the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity, effective wardrobe, and screen-right brown leather watch across the clip. Lock FLASHLIGHT's black textured body and lens, preserve its contact with both hands, and maintain the exact switch-on timing and continuous illumination.
Everything else — the original close composition, seated posture, two-handed contact placement, camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clip 1 intento 2 — APROBADO

- job_id: `f67f6dd8-39c7-4e30-b470-e9758ad5d16c`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 7 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`4513e4ed-ba6d-4132-9e23-e5a05017bb1e` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_164844_f67f6dd8-39c7-4e30-b470-e9758ad5d16c.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. Keep exactly the same close framing, do NOT zoom out. Keep his exact pose, hand position and lip movement.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; dark green shirt open over a white t-shirt.
4. WATCH: brown leather watch on HIS LEFT wrist only, which appears on the RIGHT side of the image. The wrist on the left side of the image has NO watch.
5. Replace the microphone with the flashlight from reference image 2.
6. FLASHLIGHT SWITCH-ON AT THE VERY BEGINNING OF THE VIDEO - this is the key moment:
- The video opens in near darkness with the flashlight OFF, only a faint silhouette visible, for just a brief instant (a few frames only).
- Almost immediately, at the very start, BEFORE he says his first word, his thumb presses the button and the flashlight turns ON INSTANTLY, like a real flashlight, NOT a slow fade-in. The lens glows bright at that same moment.
- The flashlight is ON for almost the ENTIRE video. Every word he says is spoken with his face lit by the flashlight. He NEVER speaks in the dark.
- Once on, it never flickers, never dims, never turns off until the last frame.
7. Lighting once ON: same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. Soft and well exposed, NOT blown out, no patches or blotches on the skin, no light patterns projected on his face. The flashlight is the ONLY light source: no key, fill or side light. Black room. His body and shirt stay very dark, almost black; only his hands catch a faint glow.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN, the replacement MAN: early-thirties man with short almost-black hair, thick eyebrows, dark brown eyes, a full neatly trimmed dark beard, and a natural medium build. Wardrobe: dark green open button-front shirt over a white T-shirt.
@Image2 and @Image3 — FLASHLIGHT, the replacement FLASHLIGHT: compact black handheld flashlight with a wide matte-black head, reflective silver lens cup, central LED, and textured cylindrical grip.
@Image4 — UNDER-LIGHTING, the replacement LIGHTING reference: black-room horror under-lighting with a softly exposed upward glow on the chin, lips, nostrils, and cheekbones; deep shadow over the eyes and forehead; dark body and surroundings.
Video edit. Keep this @Video1 clip exactly as it is — the same single 6s take, static camera, close medium framing and composition, seated blocking, direct-to-camera speaking performance, exact pose, hand placement, lip movement, pacing and timing. Change only the man, the held microphone, and the green-screen setting and illumination; do not zoom out or add any on-screen text.
1. REPLACE the original man in the white t-shirt holding the microphone (0-6s) with MAN from @Image1. Put MAN into the shot beat-for-beat to the original seated speaking performance, frontal gaze, pose, and two-handed central hold. Render MAN's short almost-black hair, thick eyebrows, dark brown eyes, full trimmed dark beard, and dark green open shirt over a white T-shirt consistently. On his left wrist only, on the right side of the image, render a brown leather watch; the wrist on the left side of the image has no watch.
2. REPLACE the original black microphone held in the man's hands (0-6s) with FLASHLIGHT from @Image2 and @Image3. Keep its position and the two-handed grip matched to the source, minimally adapting the upper thumb only to press its switch at the opening. For only the opening few frames, the black room is in near darkness and FLASHLIGHT is off, leaving only a faint silhouette; before the first spoken word, the thumb presses the switch and the lens turns on instantly. Keep FLASHLIGHT steadily on without flicker, dimming, or shutdown through the last frame.
3. REPLACE the green screen background (0-6s) with a black room. After the opening few frames, use UNDER-LIGHTING from @Image4: FLASHLIGHT is the only light source, softly lighting the chin, lips, nostrils, and cheekbones from below while the eyes and forehead remain in deep shadow. Keep the face well exposed without blown highlights, skin patches, blotches, or projected light patterns; keep the body and shirt nearly black and the hands faintly glowing.
Identity lock: MAN maps only to the man in the white t-shirt holding the microphone from 0-6s, with his complete @Image1 identity and effective wardrobe, including the specified left-wrist-only brown leather watch. Within 0-6s, replace the original source person identified as the man in the white t-shirt holding the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. MAN is never duplicated onto another figure. FLASHLIGHT maps only to the held microphone and remains protected in both hands; @Image3 is a complementary view of the same FLASHLIGHT. UNDER-LIGHTING applies only to the black-room replacement setting and follows the flashlight state.
Everything else — the original seated performance, exact close framing, positions, screen placement, Spanish speech, camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clips 5+7 intento 1 (luz plana, rechazado)

- job_id: `e9f28d46-b6fb-4e92-8d60-14a7887dedfc`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 8 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`c4a9970e-8861-4888-a048-c3e724e63377` (media_input), 5=video:`48c5104d-96e5-4d6e-a0e5-a6b938467a94` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_171858_e9f28d46-b6fb-4e92-8d60-14a7887dedfc.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. This video has TWO shots with a cut between them. Keep exactly the same framing of each shot, do NOT zoom out. Keep his exact pose, hand movements and lip movement; do NOT invent new gestures.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; dark green shirt open over a white t-shirt, black cargo pants.
4. WATCH: brown leather watch on HIS LEFT wrist only, which appears on the RIGHT side of the image. The wrist on the left side of the image has NO watch.
5. Replace the microphone with the flashlight from reference image 2.
6. The flashlight is ALREADY ON from the very first frame of BOTH shots. It never turns on, never flickers, never dims, never turns off. There is NO normal room light at any moment in either shot.
7. Lighting in BOTH shots: same horror under-lighting as reference image 4: lit chin, lips, nostrils and cheekbones, dark shadows over the eyes and forehead. Soft and well exposed, NOT blown out, no patches or blotches on the skin, no light patterns projected on his face. The flashlight is the ONLY light source: no key, fill or side light. Black room. His body, shirt and pants stay very dark, almost black; only his hands catch a faint glow.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN, the replacement MAN: early-thirties man with short almost-black hair, thick eyebrows, dark brown eyes, and a full neatly trimmed dark beard; natural medium build and photogenic appearance. Wardrobe: dark green open shirt over a white T-shirt, black cargo pants, dark shoes, and a brown leather watch on his left wrist.
@Image2 and @Image3 — FLASHLIGHT, the replacement FLASHLIGHT (two views of the same flashlight): black handheld flashlight with a wide cylindrical head, metallic reflector, and textured black grip.
@Image4 — UNDER-LIGHTING REFERENCE, the LIGHTING REFERENCE: soft horror-style upward illumination from below, lighting the chin, lips, nostrils, and cheekbones while the eyes and forehead remain in dark shadow.
Video edit. Keep this @Video1 clip exactly as it is — the same single continuous 0-7s take, the same static camera, framing and composition with no zoom out, the same centered screen placement, original Spanish speech timing, lip movement, pose, hand movements, blocking, and pacing. Change only the presenter identity and wardrobe, microphone, wristwatch, green-screen setting, and lighting; retain the original hand grip and object-contact positions while rendering the replacement man’s complete image-defined appearance and stature.
1. REPLACE the original man holding the microphone (0-7s) with MAN from @Image1. Put MAN into the full shot, matched beat-for-beat to the original direct-to-camera speaking, facial speech timing, steady two-handed hold, minor head movement, pose, and framing. Render MAN’s full declared appearance — short almost-black hair, thick eyebrows, dark brown eyes, full trimmed dark beard, dark green open shirt over a white T-shirt, and black cargo pants — consistently throughout.
2. REPLACE the original black microphone (0-7s) with FLASHLIGHT from @Image2 and @Image3. Keep it vertical in both hands at the same chest position and preserve its slight inherited hand-driven movement. The flashlight is already switched on from the first frame and remains steadily illuminated with no flicker, dimming, activation, or shutdown.
3. MODIFY only the green screen background and scene lighting (0-7s) so that the background is a black room and the lit flashlight is the sole light source, using the soft under-lighting from @Image4: illuminate the chin, lips, nostrils, and cheekbones while keeping the eyes and forehead shadowed. Keep the face softly exposed without blown highlights, skin blotches, patches, or projected patterns; leave the body, shirt, and pants nearly black, with only faint flashlight glow on the hands. Use no key, fill, side, or normal room light.
4. MODIFY only the wristwatch on MAN’s left wrist (0-7s) so that it is a brown leather watch, visible only on the right side of the image; the wrist on the left side of the image has no watch. Preserve the source ring and both-hand flashlight grip.
Identity lock: MAN belongs only to the original man holding the microphone during 0-7s and is never duplicated onto another figure. Within the entire clip, replace the original source person identified as the man holding the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person’s original appearance, subject only to other explicitly requested edits. Lock MAN’s complete image-defined identity, effective wardrobe, and left-wrist brown leather watch across the clip. Lock FLASHLIGHT from @Image2 and @Image3 as the continuously on sole light source, held at the original contact point; preserve its illumination behavior and the requested under-lighting from @Image4.
Everything else — the original Spanish speech, lip-sync timing, hand movements, ring, centered composition, static framing, the camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clips 5+7 v3 (luz dura)

- job_id: `35ed4e03-0320-4d93-af9c-a1e6fd0fd24c`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 8 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`98203286-2578-447f-8024-5c249b4c86a7` (media_input), 5=video:`48c5104d-96e5-4d6e-a0e5-a6b938467a94` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_174939_35ed4e03-0320-4d93-af9c-a1e6fd0fd24c.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. This video has TWO shots with a cut between them. Keep exactly the same framing of each shot, do NOT zoom out. Keep his exact pose, hand movements and lip movement; do NOT invent new gestures.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; dark green shirt open over a white t-shirt, black cargo pants.
4. WATCH: brown leather watch on HIS LEFT wrist only, which appears on the RIGHT side of the image. The wrist on the left side of the image has NO watch.
5. Replace the microphone with the flashlight from reference image 2.
6. The flashlight is ALREADY ON from the very first frame of BOTH shots. It never turns on, never flickers, never dims, never turns off. There is NO normal room light at any moment in either shot.
7. Lighting in BOTH shots: copy EXACTLY the lighting of reference image 4 (same character, same flashlight): HARD, high-contrast light from the flashlight below. A dark band of shadow across the forehead, deep shadows beside the nose and under the brow ridge, the sides of the face falling off into black. Lit chin, lips, nostrils and cheekbones. Defined shadows with sharp edges, NOT soft, NOT flat, NOT evenly lit. Do not blow out the highlights and no patches or blotches on the skin. The flashlight is the ONLY light source: no key, fill or side light. Black room. His body, shirt and pants stay very dark, almost black; only his hands catch a faint glow.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image4 — MAN, the replacement MAN: early-thirties man with short almost-black hair, thick eyebrows, dark brown eyes, and a full neatly trimmed dark beard; natural medium complexion and average build. Wardrobe: dark green open shirt over a white T-shirt, black cargo pants, and a brown leather watch on his anatomical left wrist only.
@Image2 and @Image3 — FLASHLIGHT, the replacement FLASHLIGHT: compact black handheld flashlight with a wide black bezel, reflective silver interior, and textured black cylindrical grip.
Video edit. Keep this @Video1 clip exactly as it is — the same shots and cuts, the same camera moves, framing and composition of each shot with no zoom out, the same seated blocking, direct-to-camera eyeline, exact pose, hand movements, speech lip movement, pacing and timing. Change only the man, microphone, left-wrist watch, green-screen setting, and lighting; preserve original positions, screen placement, hand contact, and timing.
1. REPLACE the original man speaking into the microphone (0.0-7.3s throughout) with MAN from @Image1 and @Image4. Put MAN into every appearance, matched beat-for-beat to the original direct-to-camera speech, subtle head movement, facial movement, seated pose, and clasped-hand position. Render MAN's short almost-black hair, thick eyebrows, dark brown eyes, full trimmed beard, dark green open shirt over a white T-shirt, and black cargo pants consistently. Keep both hands naturally clasping the replacement flashlight.
2. REPLACE the original black microphone with square flag (0.0-7.3s throughout) with FLASHLIGHT from @Image2 and @Image3. Keep it upright at lower-center chest height in the man's clasped hands. The flashlight is already on from the first frame of every shot and remains continuously on without flickering, dimming, turning on, or turning off.
3. MODIFY only the wristwatch on the man's left wrist (0.0-7.3s throughout) so that it is a brown leather watch on his anatomical left wrist only, appearing on the right side of the image; the wrist on the left side of the image has no watch. Preserve the ring and all hand contact.
4. MODIFY only the green screen background and scene illumination (0.0-7.3s throughout) into a black room lit exclusively by the active FLASHLIGHT from below, matching @Image4: hard high-contrast underlighting, a dark forehead-shadow band, deep shadows beside the nose and beneath the brow ridge, sharply defined facial shadows, lit chin, lips, nostrils, and cheekbones, with facial sides falling into black. No room light, key, fill, or side light; keep highlights controlled and skin even without blown patches or blotches. Keep the body, shirt, and pants almost black, with only faint flashlight glow on the hands. Do not generate subtitles, captions, or on-screen text of any kind.
Identity lock: MAN belongs only to the man speaking into the microphone for 0.0-7.3s and is never duplicated onto another figure. Within 0.0-7.3s, replace the original source person identified as the man speaking into the microphone in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity, effective wardrobe, and left-wrist-only brown leather watch across all frames and shots. Lock FLASHLIGHT's form, illuminated state, and two-handed contact; its light and the black-room shadows follow it continuously.
Everything else — the seated position, hand movements, ring, speech audio, exact lip sync, framing, composition, camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clip 3 (sin reloj)

- job_id: `012981eb-fbef-458f-9bd5-0b1dfe056fa9`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 12 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`469788cb-32d8-4d01-9858-a386584ee346` (image_job), 4=image:`98203286-2578-447f-8024-5c249b4c86a7` (media_input), 5=video:`1c507291-9178-4a6e-8c1c-b222bf7e9591` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_182109_012981eb-fbef-458f-9bd5-0b1dfe056fa9.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. Keep exactly the same close framing, do NOT zoom out. Keep his exact pose, hand movements and lip movement; do NOT invent new gestures. His clasped hands stay at the same height as in the source video, about three quarters down the frame, in front of his chest; the hands must NOT drop to his stomach or lap.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; dark green shirt open over a white t-shirt.
4. WATCH: brown leather watch on HIS LEFT wrist only, which appears on the RIGHT side of the image. The wrist on the left side of the image has NO watch.
5. Replace the microphone with the flashlight from reference image 2.
6. The flashlight is ALREADY ON from the very first frame. It never turns on, never flickers, never dims, never turns off. There is NO normal room light at any moment.
7. Lighting: copy EXACTLY the lighting of reference image 4 (same character, same flashlight): HARD, high-contrast light from the flashlight below. A dark band of shadow across the forehead, deep shadows beside the nose and under the brow ridge, the sides of the face falling off into black. Lit chin, lips, nostrils and cheekbones. Defined shadows with sharp edges, NOT soft, NOT flat, NOT evenly lit. Do not blow out the highlights and no patches or blotches on the skin. The flashlight is the ONLY light source: no key, fill or side light. Black room. His body and shirt stay very dark, almost black; only his hands catch a faint glow.
```

Prompt mejorado por Higgsfield:

```text
@Image1 and @Image4 — MAN A, the replacement MAN (complementary identity and lighting views): early-thirties man with light-to-medium olive skin, short almost-black hair, thick eyebrows, dark brown eyes, and a full neatly trimmed dark beard. Wardrobe: dark green open button-front shirt over a white T-shirt, dark trousers; brown leather watch on his left wrist only.
@Image2 and @Image3 — FLASHLIGHT, the replacement HANDHELD PROP (two views): compact black metal flashlight with a wide circular bezel, reflective lens, and knurled cylindrical grip.
Video edit. Keep this @Video1 clip exactly as it is — the same single continuous 10.7s take, static close vertical framing and composition with no zoom out, the same seated pose, direct-to-camera Spanish speaking performance, lip movement, hand movements, clasped hand height three quarters down the frame in front of the chest, blocking, pacing and timing. Change only the man, handheld microphone, left-wrist watch, green background, and illumination; do not introduce gestures or move the hands to the stomach or lap.
1. REPLACE the original man in the white t-shirt holding the microphone (0-10.7s) with MAN A from @Image1 and @Image4. Put MAN A into the full shot, matched beat-for-beat to the original seated speaking performance and two-handed chest-level grip. Render MAN A's short almost-black hair, thick eyebrows, dark brown eyes, trimmed full beard, olive skin, and dark green open shirt over a white T-shirt consistently across the shot.
2. REPLACE the black handheld microphone with FLASHLIGHT from @Image2 and @Image3 (0-10.7s). Keep it held in the same two-handed position at chest level, with the flashlight already continuously on from the first frame.
3. MODIFY only the watch on the man's left wrist, appearing on the right side of the image (0-10.7s), so that it is MAN A's brown leather watch; leave the wrist on the left side of the image without any watch.
4. MODIFY only the green screen background and scene illumination (0-10.7s) into a black room lit solely by the active flashlight from below, exactly matching @Image4: hard high-contrast upward light, a dark forehead shadow band, deep shadows beside the nose and under the brow ridge, face sides falling into black, and sharply defined light on the chin, lips, nostrils, and cheekbones. Keep highlights controlled and skin natural without blotches; the body and shirt remain almost black and only the hands receive faint glow. No room, key, fill, or side light is present.
Identity lock: MAN A replaces only the man in the white t-shirt holding the microphone for 0-10.7s; lock his complete image-defined identity, dark green shirt outfit, and left-wrist brown leather watch. Within 0-10.7s, replace the original source person identified as the man in the white t-shirt holding the microphone in @Video1 completely with MAN A in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. MAN A is never duplicated onto another figure. Keep FLASHLIGHT continuously illuminated without flicker, dimming, switching on, or switching off, and preserve its two-hand contact. Do not create subtitles, captions, or on-screen text.
Everything else — the unseen seat support, original speech timing, camera moves and all timing — stays exactly the same.
```

## Felipe 2.0 · Clip 8 prueba 480p efecto luces graduales (falló)

- job_id: `9aecefb9-f196-49bd-9775-5b265afa59f9`
- modelo: `hf_mult_replace_object` · resolución: 480p · duración: 11 · aspecto: auto
- medias: 1=image:`62f9daf0-4599-4c89-8e7a-21bab4a20939` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`4ff7ac26-8d20-4466-885c-341a1cbf4351` (image_job), 4=image:`5d9d0388-72f8-48b5-987a-d4c6b8635d43` (image_job), 5=image:`1f823f09-4d4a-478d-9976-abddb7149d39` (media_input), 6=video:`83043a0f-a861-45eb-8d9d-f5e8eacb8cf1` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_185349_9aecefb9-f196-49bd-9775-5b265afa59f9.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. Keep the camera movement (a smooth continuous pull-back with no cuts or jumps), framing, body movement, the action of standing up, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick eyebrows, dark brown eyes, full dark trimmed beard; very dark green button-down shirt worn open over a white crew-neck t-shirt, pure black cargo pants, black sneakers, no bracelets. WATCH: brown leather watch on HIS LEFT wrist only, which appears on the RIGHT side of the image.
4. Replace the microphone with the flashlight from reference image 2, switched OFF, in every frame. He holds it and sets it down exactly the same way.
5. Replace the black box he sits on with the walnut armchair with gray cushion from reference image 3; he stands up from this armchair.
6. Replace the tall wooden stool with the tall round table from reference image 4: walnut round top, single black column, round black base, same position. The flashlight rests on its top.
7. Replace the whole green screen studio with the showroom interior from reference image 5: warm brown plaster walls, curved ceiling with recessed spotlights and a large round ceiling cove, floor-to-ceiling windows with sheer white curtains, green plants in white pots, polished gray concrete floor with thin dark curved inlaid lines. No green anywhere.
8. REMOVE the white chair that peeks in at the bottom-left corner of the frame; show the concrete floor there instead.
9. LIGHTING EVENT (key moment): the showroom starts DIM with all the ceiling spotlights OFF, only soft daylight from the windows. Right after he sets the flashlight down on the table, the recessed ceiling spotlights switch ON one row at a time, from the closest row to the farthest, each one with a quick soft glow. NOT all at once, NOT a global fade of the whole room. EVERY spotlight is already ON by the moment he brings both hands together in front of his chest, early in the shot. From then until the end the room is fully lit, warm and natural like reference image 5. His face and clothes stay naturally lit the whole time.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN A, the replacement MAN: early-thirties man with light-to-medium skin, short almost-black hair, thick eyebrows, dark brown eyes, and a full trimmed dark beard; average stature and build. Wardrobe: very dark green open button-down over a white crew-neck T-shirt, pure black cargo pants, black sneakers, no bracelets, and a brown leather watch on his left wrist only.
@Image2 — FLASHLIGHT, the replacement PRODUCT: compact black handheld flashlight with a broad circular bezel, reflective silver interior, and textured cylindrical grip; switched off.
@Image3 — ARMCHAIR, the replacement OBJECT: walnut wood armchair with rounded arms and a gray upholstered seat and back cushion.
@Image4 — TABLE, the replacement OBJECT: tall round table with a walnut round top, single black column, and round black base.
@Image5 — SHOWROOM, the replacement LOCATION: warm brown plaster showroom interior with a curved ceiling, recessed spotlights, a large round ceiling cove, floor-to-ceiling windows with sheer white curtains, green plants in white pots, and polished gray concrete flooring with thin dark curved inlaid lines.
Video edit. Keep this @Video1 clip exactly as it is — the same single continuous 9.5-second take, smooth continuous pull-back with no cuts or jumps, framing and composition, Spanish dialogue, performance, standing action, body movement, gestures, head movement, mouth and lip movement, blocking, positions, pacing and timing. Change only the presenter, microphone, gear case, stool, studio, bottom-left white chair, on-screen text, and the requested ceiling-light event; retain no on-screen text of any kind.
1. REPLACE the original man in the white t-shirt (0.0-9.5s) with MAN A from @Image1. Put MAN A into the entire take, matched beat-for-beat to the original seated speaking, setting down the held object, standing, and gesturing. Render MAN A's short almost-black hair, thick eyebrows, dark brown eyes, trimmed full dark beard, dark green open shirt over white T-shirt, black cargo pants, black sneakers, and brown leather watch on his left wrist only, appearing on the right side of the image. Keep his appearance consistent throughout.
2. REPLACE the original black microphone in the man's right hand (0.0-9.5s) with FLASHLIGHT from @Image2, switched off. He holds it until 0.9s and sets it onto the table top during 0.9-1.5s; it remains resting there afterward with natural contact and shadow.
3. REPLACE the original black rolling gear case (0.0-9.5s) with ARMCHAIR from @Image3. MAN A begins seated in the armchair and stands from it at the same source moment.
4. REPLACE the original wooden stool on screen left (0.0-9.5s) with TABLE from @Image4 in the same position. The flashlight rests on its walnut top after being set down.
5. REPLACE the original green screen room (0.0-9.5s) with SHOWROOM from @Image5. Preserve the source spatial blocking and floor contact; show no green anywhere.
6. REMOVE only the white chair peeking into the bottom-left corner (0.0-9.5s) and reconstruct the polished concrete floor there consistently with its immediate surroundings and curved inlaid lines.
7. REMOVE only any captions, subtitles, and other on-screen text (0.0-9.5s), leaving clean footage beneath.
8. MODIFY only the SHOWROOM recessed ceiling spotlights (immediately after the flashlight is set down during 0.9-1.5s through the first source moment when both hands come together in front of his chest) so the room begins dim with all spotlights off and soft window daylight only, then the spotlights turn on one row at a time from closest to farthest with quick soft individual glows. Every spotlight is on by that hands-together moment; afterward the showroom remains warmly and naturally lit. Do not use an all-at-once activation or global room fade; keep MAN A's face and clothing naturally lit throughout.
Identity lock: MAN A replaces only the man in the white t-shirt for 0.0-9.5s; FLASHLIGHT replaces only the microphone, ARMCHAIR only the gear case, TABLE only the stool, and SHOWROOM only the green screen room. Within 0.0-9.5s, replace the original source person identified as the man in the white t-shirt in @Video1 completely with MAN A in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN A's complete image-defined identity and wardrobe across the take; do not duplicate MAN A onto another figure. Keep the flashlight, armchair, table, floor contacts, occlusions, and shadows consistent with their mapped references.
Everything else — the Spanish dialogue, source performance timing, continuous camera pull-back, framing, composition, and all timing — stays exactly the same.
```

## Felipe 2.0 · Clip 8 720p versión normal — usado (silla borrada en edición)

- job_id: `999e9363-d0f0-407a-9109-de9bbab1dc4e`
- modelo: `hf_mult_replace_object` · resolución: 720p · duración: 11 · aspecto: auto
- medias: 1=image:`1c3921d4-dd74-445a-8f6a-ad3331959083` (media_input), 2=image:`7b3f9522-f0cd-4768-92d7-49c4d8615462` (image_job), 3=image:`4ff7ac26-8d20-4466-885c-341a1cbf4351` (image_job), 4=image:`5d9d0388-72f8-48b5-987a-d4c6b8635d43` (image_job), 5=image:`1f823f09-4d4a-478d-9976-abddb7149d39` (media_input), 6=video:`83043a0f-a861-45eb-8d9d-f5e8eacb8cf1` (video_input)
- resultado: https://d8j0ntlcm91z4.cloudfront.net/user_3B7wyzz5dVFJbi5BZFerYlwgD2L/hf_20261005_194803_999e9363-d0f0-407a-9109-de9bbab1dc4e.mp4

```text
1. NO subtitles, NO captions, NO on-screen text of any kind.
2. Keep the camera movement (a smooth continuous pull-back with no cuts or jumps), framing, body movement, the action of standing up, hand gestures, head movement, mouth and lip movement while talking, and timing exactly the same as the source video.
3. Replace the man with the character from reference image 1: early thirties, short almost-black hair, thick neatly groomed eyebrows, dark brown eyes, full dark trimmed beard; very dark green button-down shirt worn open over a white crew-neck t-shirt, pure black cargo pants, black sneakers, no bracelets. WATCH: brown leather watch on HIS LEFT wrist only, which appears on the RIGHT side of the image.
4. Replace the microphone with the flashlight from reference image 2, switched OFF, in every frame. He holds it and sets it down exactly the same way.
5. Replace the black box he sits on with the walnut armchair with gray cushion from reference image 3; he stands up from this armchair.
6. Replace the tall wooden stool with the tall round table from reference image 4: walnut round top, single black column, round black base, same position. The flashlight rests on its top.
7. Replace the whole green screen studio with the showroom interior from reference image 5: warm brown plaster walls, curved ceiling with recessed spotlights and a large round ceiling cove, floor-to-ceiling windows with sheer white curtains, green plants in white pots, polished gray concrete floor with thin dark curved inlaid lines. As the camera pulls back, more of the showroom and its ceiling is revealed. No green anywhere.
8. REMOVE the white chair that peeks in at the bottom-left corner of the frame; show the concrete floor there instead.
9. Lighting: normal, warm and natural like reference image 5, daylight from the windows plus the ceiling spotlights ON the whole time. Not dark, not horror.
```

Prompt mejorado por Higgsfield:

```text
@Image1 — MAN, the replacement MAN: early-thirties man with light-medium olive skin, short almost-black hair, thick neatly groomed eyebrows, dark brown eyes, and a full neatly trimmed dark beard. Wardrobe: very dark green open button-down shirt over a white crew-neck T-shirt, pure black cargo pants, black sneakers, no bracelets, and a brown leather watch on his left wrist only (screen right).
@Image2 — FLASHLIGHT, the replacement FLASHLIGHT: black handheld flashlight with a broad round reflector head, metallic inner reflector, and textured black cylindrical grip; switched off.
@Image3 — ARMCHAIR, the replacement ARMCHAIR: warm walnut wood frame with rounded arms and gray upholstered seat and back cushions.
@Image4 — TABLE, the replacement TABLE: tall round walnut tabletop on a single black column with a round black base.
@Image5 — SHOWROOM, the replacement LOCATION: warm brown plaster walls, a curved ceiling with recessed spotlights and a large round ceiling cove, floor-to-ceiling windows with sheer white curtains, green plants in white pots, and polished gray concrete flooring with thin dark curved inlaid lines.
Video edit. Keep this @Video1 clip exactly as it is — the same single continuous 0-9s take, smooth pull-back camera movement, framing and composition, spoken performance, standing action, body and head movement, hand gestures, mouth and lip movement, blocking, pacing and timing. Change only the man, microphone, equipment case, barstool, studio setting, any on-screen text, and the white chair at bottom left; retain the exact object interactions and positions while rendering each replacement person's complete image-defined appearance and stature.
1. REPLACE the original man speaking in the white t-shirt (0-9s) with MAN from @Image1. Put MAN into the full take, matched beat-for-beat to the original seated lean, stand, direct-to-camera speech, gestures, and placement actions. Render MAN's full declared appearance — short almost-black hair, thick groomed eyebrows, dark brown eyes, trimmed full beard, dark green open shirt over white T-shirt, black cargo pants, black sneakers, and brown leather watch only on his left wrist, visible screen right. Keep his face and wardrobe consistent throughout.
2. REPLACE the original black handheld microphone (0-9s) with FLASHLIGHT from @Image2. Keep it switched off in every frame; MAN holds it and sets it horizontally on the table at the identical time and contact point.
3. REPLACE the original black rolling equipment case (0-9s) with ARMCHAIR from @Image3. Keep the armchair in the same source position and have MAN stand up from it on the same beat.
4. REPLACE the original barstool (0-9s) with TABLE from @Image4 in the same screen-left position. The flashlight rests on its walnut top after placement.
5. REPLACE the original green-screen room (0-9s) with SHOWROOM from @Image5. Reveal more of the showroom and ceiling naturally during the pull-back; use warm natural daylight from the windows plus illuminated ceiling spotlights throughout, with no green visible.
6. REMOVE only all captions, subtitles, and other on-screen text (0-9s), leaving clean imagery beneath.
7. REMOVE only the white chair peeking into the bottom-left corner (wherever visible in the take) and reconstruct the polished concrete floor consistently from its immediate surroundings.
Identity lock: MAN maps only to the original man speaking in the white t-shirt for 0-9s and is never duplicated onto another figure. Within 0-9s, replace the original source person identified as the man speaking in the white t-shirt in @Video1 completely with MAN in every appearance; the original identity must not appear within those windows. Retain the original performance, pose, blocking, interactions, and timing. Outside those windows, preserve that source person's original appearance, subject only to other explicitly requested edits. Lock MAN's complete image-defined identity and effective wardrobe across the take, including no bracelets and the brown leather watch on his left wrist only. Protect the flashlight hand contact, tabletop placement, armchair contact, floor contact, and all corresponding shadows.
Everything else — the uninterrupted Spanish speech timing, precise pull-back, source movement, object contact timing, and all untargeted elements, the camera moves and all timing — stays exactly the same.
```
