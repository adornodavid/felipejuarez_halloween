---
name: elevenlabs-instalado
description: "ElevenLabs instalado 29 sep 2026 — MCP \"elevenlabs\" (user scope), SDK Python y ELEVENLABS_API_KEY en ~/.zshrc; la key no tiene permiso user_read"
metadata:
  node_type: memory
  type: reference
  originSessionId: 85d3685b-3bf5-435d-b13f-6aeb1799601b
  modified: 2026-09-29T17:27:29.948Z
---

- MCP `elevenlabs` en scope user: `~/Library/Python/3.9/bin/uvx elevenlabs-mcp`, con salida en ~/Downloads/CLAUDE (ver [[entregas-carpeta-claude]]).
- SDK Python `elevenlabs` 2.70 instalado con `pip3 --user` (Python 3.9 del sistema); uv/uvx viven en ~/Library/Python/3.9/bin (no está en PATH).
- `ELEVENLABS_API_KEY` exportada en ~/.zshrc.
- La key **no tiene el permiso `user_read`**: `/v1/user/subscription` da 401, así que no se pueden consultar los créditos por API. Las voces y el TTS sí funcionan (eleven_multilingual_v2 probado).
- En la cuenta hay voces propias: "CAVA11 Avatar (Seedance) - crowne aquisi", "Camila", "Gaby - Young Student".

**Cambio de voz (speech-to-speech) que funciona (2 oct 2026, Terra Regia):** la herramienta MCP `speech_to_speech` solo acepta voces de la cuenta por nombre; para voces de la biblioteca compartida llamar directo `POST /v1/speech-to-speech/{voice_id}` con `model_id=eleven_multilingual_sts_v2` (no hace falta agregarlas a la cuenta). Conserva duración y pausas (desfase 0 s medido) → los labios siguen cuadrando. Sale ~4 LUFS más fuerte que la entrada. Para buscar voces con filtros reales usar `GET /v1/shared-voices?gender=male&age=old&language=es&search=...` (el search del MCP es muy limitado). Liz eligió **Arturo Casares** (`N2HSRirbsHTZ8DE2WqjB`, hombre mayor, suspenso) para el personaje canoso; descartó Salvatore, El Faraón y Josué Maya.
