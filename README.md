# Voice AI Tutor - FastAPI Backend

This project is the backend for a voice-based AI tutor. It provides endpoints for real-time conversation, memory storage, and recall using a graph database.

## Project Structure

voice-ai-tutor/
├── backend/
│   ├── main.py         # FastAPI entrypoint
│   ├── graph.py        # Neo4j helper
│   ├── ai_engine.py    # GPT-based tutor logic
│   ├── stt.py          # Whisper integration
│   └── tts.py          # ElevenLabs / Web Speech output
├── frontend/
│   ├── index.html
│   └── app.js          # Voice UI (React or Vanilla JS)
├── README.md
├── requirements.txt
└── .gitignore

## Features
- `/ask`: Accepts user input, transcribes voice, and generates AI responses
- `/remember`: Stores concepts and context in a Neo4j graph database
- `/recall`: Fetches user's past learning nodes from Neo4j

## Stack
- Python 3.10+
- FastAPI
- Neo4j (via neo4j-driver)
- OpenAI API (for GPT-4o)
- Whisper API (for STT)

## Setup
1. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Set environment variables for API keys and Neo4j connection.
4. Run the server:
   ```powershell
   uvicorn backend.main:app --reload
   ```

## Endpoints
- `POST /ask`: Accepts audio or text, returns AI response
- `POST /remember`: Stores a concept/context
- `GET /recall`: Returns user's learning nodes

---
