from backend.voice import record_audio
from backend.transcribe import transcribe_audio
from backend.llm import query_llm
from backend.tts import speak

def main_loop():
    """
    Conversational loop: records audio, transcribes, queries LLM, and speaks response.
    """
    print("[Loop] Starting voice assistant. Press Ctrl+C to exit.")
    while True:
        record_audio()
        text = transcribe_audio()
        print(f"[User] {text}")
        response = query_llm(text)
        print(f"[Assistant] {response}")
        speak(response)
