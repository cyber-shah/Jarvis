import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name} - {voice.id}")

# Choose a voice explicitly (for example, the first one)
engine.setProperty('voice', voices[0].id)

engine.say("Hello! Jarvis is ready to speak.")
engine.runAndWait()
