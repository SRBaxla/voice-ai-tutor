import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record_audio(filename="input.wav", duration=5, fs=16000):
    """
    Records audio from the default microphone and saves it as a WAV file.
    """
    print(f"[Voice] Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, audio)
    print(f"[Voice] Audio saved to {filename}")
