# Anthropic Courses

Ejercicios y notas de los cursos oficiales de la [plataforma Claude](https://claude.com/resources/courses).

## Cursos

| Curso | Estado | Carpeta |
|-------|--------|---------|
| [Building with the Claude API](#) | 🟡 En progreso | [Building with the Claude API/](Building%20with%20the%20Claude%20API/) |
| Claude with Amazon Bedrock | ⬜ Pendiente | — |
| Claude with Google Cloud's Vertex AI | ⬜ Pendiente | — |

## Requisitos generales

- Python 3.10+
- `anthropic` SDK
- `python-dotenv`
- Archivo `.env` con `ANTHROPIC_API_KEY`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
```

Crear un archivo `.env` en la carpeta del curso:

```
ANTHROPIC_API_KEY=sk-ant-...
```
