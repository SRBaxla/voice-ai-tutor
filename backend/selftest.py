import importlib
import sys

def run_self_test():
    """
    Runs a basic self-test for all core modules and reports status.
    Returns True if all tests pass, False otherwise.
    """
    modules = [
        ("sounddevice", "voice recording"),
        ("scipy.io.wavfile", "WAV file I/O"),
        ("whisper", "audio transcription"),
        ("requests", "HTTP requests"),
        ("pyttsx3", "text-to-speech")
    ]
    failed = []
    for mod, desc in modules:
        try:
            importlib.import_module(mod)
            print(f"[SelfTest] {desc}: OK")
        except Exception as e:
            print(f"[SelfTest] {desc}: FAIL ({e})")
            failed.append((mod, str(e)))
    if failed:
        print("\n[SelfTest] One or more dependencies failed. Please check your environment.")
        for mod, err in failed:
            print(f" - {mod}: {err}")
        return False
    print("[SelfTest] All dependencies OK.")
    return True
