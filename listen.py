import sounddevice as sd
import numpy as np
import whisper
import time

# Load Whisper model
model = whisper.load_model("base")

# Wake words
WAKE_WORDS = ["jarvis", "computer", "buddy", "alpha"]

def listen(duration=4, fs=16000):
    """
    Records audio from the microphone and transcribes to text using Whisper
    """
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    audio = np.squeeze(audio)
    result = model.transcribe(audio)
    text = result.get("text", "").lower()
    return text

def wait_for_wakeword():
    """
    Waits until any wake word is detected
    """
    print(f"Waiting for wake word ({', '.join(WAKE_WORDS)})...")
    while True:
        text = listen(duration=4)
        if not text:
            continue  # ignore empty transcriptions
        print("Heard:", text)
        for word in WAKE_WORDS:
            if word in text:
                print(f"Wake word '{word}' detected!")
                return
        time.sleep(0.2)
