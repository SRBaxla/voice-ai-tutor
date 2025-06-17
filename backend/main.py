from backend.voice import record_audio
from backend.transcribe import transcribe_audio
from backend.llm import query_llm
from backend.loop import main_loop
from backend.selftest import run_self_test

def main():
    print("Recording audio...")
    audio = record_audio()
    print("Transcribing audio...")
    text = transcribe_audio(audio)
    print(f"You said: {text}")
    print("Querying LLM...")
    response = query_llm(text)
    print(f"LLM response: {response}")

if __name__ == "__main__":
    if not run_self_test():
        print("[Startup] Self-test failed. Exiting.")
        exit(1)
    main_loop()
    main()
