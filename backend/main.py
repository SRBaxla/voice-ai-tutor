from fastapi import FastAPI
from backend.graph import GraphHelper
from backend.ai_engine import TutorAI
from backend.stt import transcribe_audio
from backend.tts import synthesize_speech

app = FastAPI()

graph_helper = GraphHelper()
tutor_ai = TutorAI()

@app.post("/ask")
async def ask(user_id: str, audio: bytes = None, text: str = None):
    # If audio, transcribe
    if audio:
        text = transcribe_audio(audio)
    # Get AI response
    response = tutor_ai.get_response(user_id, text)
    return {"response": response}

@app.post("/remember")
async def remember(user_id: str, concept: str, context: str = None):
    graph_helper.remember_concept(user_id, concept, context)
    return {"status": "Concept remembered."}

@app.get("/recall")
async def recall(user_id: str):
    nodes = graph_helper.recall_concepts(user_id)
    return {"nodes": nodes}
