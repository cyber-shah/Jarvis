# 🤖 Jarvis — Your Local AI Assistant

> Voice-activated. Offline. No subscriptions. No cloud. Just you and your machine.

Jarvis is a fully local AI assistant powered by [Ollama](https://ollama.com) and Llama 3. It listens to your voice, thinks locally, and talks back — all without sending a single byte to the internet. No API keys. No monthly fees. Your own Iron Man moment, running on your own hardware.

---

## ✨ What It Can Do

- 🎙️ **Voice activated** — just speak, no typing required
- 💬 **Answers questions** — powered by Llama 3 running fully on-device
- 🖥️ **Controls your computer** — open apps, manage files, and more
- 🎵 **Plays music** — voice-controlled media playback
- ⏰ **Sets reminders & timers** — hands-free scheduling
- 🔍 **Searches the web** — pulls information without leaving the terminal
- 🔒 **100% private** — nothing leaves your machine, ever

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| AI Model | Llama 3 via Ollama |
| Language | Python |
| Voice Input | Speech Recognition |
| Voice Output | Text-to-Speech (TTS) |
| Platform | Windows |

---

## ⚙️ Prerequisites

Before you start, make sure you have:

- Windows 10 or 11
- Python 3.10+
- [Ollama](https://ollama.com) installed
- A microphone

---

## 🚀 Installation

**1. Clone the repo**
```bash
git clone https://github.com/cyber-shah/jarvis
cd jarvis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Pull the Llama 3 model via Ollama**
```bash
ollama pull llama3
```

**4. Run Jarvis**
```bash
python jarvis.py
```

Jarvis will start listening. Just speak naturally.

---

## 🎙️ Example Commands

```
"Hey Jarvis, what's the capital of Japan?"
"Jarvis, open Spotify"
"Set a timer for 25 minutes"
"Search for the latest news on AI"
"Play some lo-fi music"
```

---

## 📁 Project Structure

```
jarvis/
├── jarvis.py          ← Main entry point
├── voice.py           ← Speech recognition & TTS
├── brain.py           ← Ollama / Llama 3 integration
├── commands.py        ← Computer control & actions
├── requirements.txt   ← Dependencies
└── README.md
```

---

## 🔧 Configuration

You can tweak Jarvis in `jarvis.py`:

```python
MODEL = "llama3"          # Change to any Ollama model
WAKE_WORD = "jarvis"      # Change the trigger word
VOICE_SPEED = 175         # TTS speaking rate
```

To use a different model, just pull it with Ollama:
```bash
ollama pull mistral
```
Then update `MODEL = "mistral"` in the config.

---

## 💡 Why I Built This

Cloud assistants are convenient but they come with tradeoffs — your conversations are sent to external servers, there's latency on every request, and you're dependent on a subscription staying alive. I wanted something that was mine. Fully local, fully private, and fast. Jarvis runs entirely on my machine and responds in seconds.

---

## 🚀 Roadmap

- [ ] Memory — remember context across sessions
- [ ] Custom wake word training
- [ ] Linux & Mac support
- [ ] GUI dashboard
- [ ] Plugin system for custom commands

---

## 📄 License

MIT — do whatever you want with it.

---

*Built by [Aaryan Shah](https://github.com/cyber-shah)*
