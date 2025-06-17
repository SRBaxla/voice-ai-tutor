import whisper

def transcribe_audio(filename="input.wav") -> str:
    """
    Transcribes the given WAV file using OpenAI Whisper (local).
    """
    print(f"[Transcribe] Transcribing {filename}...")
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    text = result["text"].strip()
    print(f"[Transcribe] Transcription: {text}")
    return text
