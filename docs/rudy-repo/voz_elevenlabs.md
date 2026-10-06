# Voz (ElevenLabs)

## Método: speech-to-speech

Se cambia la voz del actor y se conservan su duración, sus pausas y su sincronía con los labios.

```bash
curl -X POST "https://api.elevenlabs.io/v1/speech-to-speech/<VOICE_ID>?output_format=mp3_44100_128" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -F "audio=@voz_original.wav" -F "model_id=eleven_multilingual_sts_v2"
```

- **Voces de la biblioteca pública:**
  - se usan directo por ID, sin agregarlas a la cuenta;
  - el MCP `speech_to_speech` solo acepta voces de la cuenta;
  - para encontrar una por ID: `GET /v1/shared-voices?search=<voice_id>`. `get_voice` da `voice_not_found` con estas voces.
- **Cómo se armó:**
  1. extraer el audio con ffmpeg (`voz_original.wav`);
  2. pasarlo por STS;
  3. volver a montarlo sobre el video con `-map 0:v -map 1:a -c:v copy`.
- **Desfase y volumen:** el desfase medido es de 0 s. La salida suele quedar unos 4 LUFS más fuerte; con Jonas quedó igual (−22.8 contra −22.6 LUFS).

## Voces

| Voz | ID | Uso |
|---|---|---|
| **Arturo Casares** | `N2HSRirbsHTZ8DE2WqjB` | Elegida para el Felipe 1.0 (hombre mayor, suspenso). Brief de Liz: "serio, elegante, 50-60 años, clara y tenebrosa" |
| **Jonas – Mexican** | `UEVUUEpjHAbzM7B6Byeu` | Probada para Felipe 2.0 (mediana edad, narración calmada): `02_felipe-juarez-2.0/voz/Video Solo voz - Jonas.mp4`. **Falta la opinión de Liz** |

- **Descartadas:** Salvatore, El Faraón, Josué Maya.
- **Rondas de prueba:** en `01_felipe-juarez-1.0_voz/` (`ronda1/`, `ronda3/` y las A–H).
