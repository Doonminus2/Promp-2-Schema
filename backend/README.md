# Prompt-2-Schema (Backend)

FastAPI backend that uses Google Gemini API to convert plain text requirements into a valid `schema.prisma` file.

## Tech Stack
- **Framework:** FastAPI
- **Package Manager:** `uv`
- **AI Model:** Google Gemini API

## Installation

1. Navigate to the backend directory:
   ```bash
   cd prompt-2-schema/backend
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Create a .env file from .env.example:
   ```bash  
   cp .env.example .env
   ```

4. Add your Gemini API key to the .env file:
   ```bash
   GEMINI_API_KEY="your_api_key"
   ```

## Run the development server: 
   ```bash
   uv run fastapi dev main.py
   ```
   Server: http://localhost:8000
   API Docs (Swagger UI): http://localhost:8000/docs

## Run in production
   ```bash
   uv run fastapi run main.py
   ```

## Build the Docker image with
``` bash 
docker build -t fastapi-app .
```
## Run the Docker container locally with:
``` bash
docker run -p 8000:80 fastapi-app
```