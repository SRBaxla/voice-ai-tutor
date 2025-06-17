# 🎓 Local Voice AI Tutor

A private, locally hosted AI tutor that learns from you. Uses voice, local models, and a personal knowledge graph to offer tailored, evolving guidance. Runs 100% offline in Docker.

---

# Local Voice-Based AI Assistant

This project captures voice from your microphone, transcribes it with Whisper, and sends the text to a local Mistral 7B model for intelligent responses—all running in Docker locally.

## How It Works
1. User speaks → Microphone records
2. Whisper (faster-whisper) transcribes speech to text
3. Local LLM (Mistral 7B, Ollama, LM Studio, etc.) receives prompt and responds

---

## 🚀 Project Overview

**Local Voice AI Tutor** is your private Jarvis.

* 🎤 Talk to it using your voice.
* 🚣️ It speaks back—live.
* 🧠 It remembers you via a growing **personal knowledge graph**.
* 📚 It answers based on your own **uploaded documents** and past interactions.
* 🔒 It’s all local—your data never leaves your machine.

Perfect for self-learners, researchers, and anyone who wants a **personal tutor that grows with them**.

---

## 🔧 Features

| Feature            | Description                                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| 🧠 Custom LLM      | Run offline using [Ollama](https://ollama.com), [LM Studio](https://lmstudio.ai), or [OpenLLM](https://github.com/bentoml/OpenLLM) |
| 🧹 RAG Support     | Load PDFs/notes as knowledge base                                                                                                  |
| 🧠 Personal Graph  | Neo4j or GraphDB to track your interests and learning                                                                              |
| 🧘 Voice Interface | Whisper STT + TTS (offline TTS like Piper or Coqui supported)                                                                      |
| 🐳 Docker Ready    | One command to deploy locally with privacy-first setup                                                                             |

---

## 📦 Project Structure

```
voice-ai-tutor/
├── backend/
│   ├── main.py           # FastAPI API server / CLI
│   ├── vector_store.py   # Local RAG index (e.g. ChromaDB)
│   ├── graph_memory.py   # Knowledge graph logic (Neo4j, RDF, etc.)
│   ├── ai_core.py        # Local LLM + prompt logic
│   ├── stt.py            # Whisper (offline) transcription
│   ├── tts.py            # Offline TTS (Piper/Coqui)
├── frontend/
│   ├── index.html
│   └── app.js            # Mic UI and voice loop
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🐳 Quickstart (Docker)

```bash
git clone https://github.com/yourname/voice-ai-tutor.git
cd voice-ai-tutor
cp .env.example .env

docker build -t voice-assistant .
docker run --rm -it --device /dev/snd voice-assistant
# Or start everything
# docker-compose up --build
```

> **Note**: Make sure you have Ollama or a compatible LLM running locally in the container (e.g., `llama3`, `mistral`, or `phi`).

---

## ⚙️ Custom Knowledge Base

Place your PDFs, Markdown, and notes in the `/knowledge_base` folder. The system will automatically ingest and create a local vector store using Chroma or FAISS.

---

## 📊 Personal Knowledge Graph

Every conversation updates a user-specific graph that includes:

* Topics learned
* Questions asked
* Strengths/weaknesses
* Suggested next topics

You can visualize this graph using Neo4j Desktop or other tools.

---

## 🧪 Sample `.env.example`

```env
MODEL_NAME=llama3
VECTOR_DB_PATH=./vector_store
KNOWLEDGE_BASE_PATH=./knowledge_base
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

---

## 🛠️ Requirements

- Python 3.10
- Docker
- Microphone access
- Locally running LLM (Ollama, LM Studio, etc.)
- [Whisper](https://github.com/openai/whisper) (local)
- Optional: Ollama or LM Studio for local LLM

---

## 📈 Roadmap

* [x] Dockerize local LLM + voice loop
* [x] Custom document ingestion with RAG
* [x] Personal knowledge graph via Neo4j
* [ ] Skill assessment + adaptive curriculum
* [ ] Voice emotion detection
* [ ] Plugin architecture (math, code, language learning)

---

## 🔐 Privacy Note

All user data stays on your machine. No cloud calls. Perfect for learning without surveillance.

---

## 📜 License

MIT License – build, remix, extend. Just don’t let it forget who taught it 🫠
