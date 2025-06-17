import pyttsx3

# Placeholder for ElevenLabs or Web Speech API integration

def synthesize_speech(text: str) -> bytes:
    # TODO: Integrate ElevenLabs or Web Speech API
    # For now, return dummy bytes
    return b"AUDIO_BYTES"

def speak(text: str):
    """
    Uses pyttsx3 to read out the response aloud.
    """
    print(f"[TTS] Speaking: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
