import subprocess
import os
import time
from listen import listen, wait_for_wakeword
from speak import speak

def ask_ai(prompt):
    """
    Sends the prompt to Ollama and returns the response safely
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral:7b-instruct"],  # update model if different
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def run_command(command):
    """
    Handles system commands
    """
    cmd = command.lower()

    if "open chrome" in cmd:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path])
        else:
            subprocess.Popen("chrome", shell=True)
        return "Opening Chrome"

    elif "open notepad" in cmd:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad"

    elif "create folder" in cmd:
        folder_name = cmd.replace("create folder", "").strip()
        if folder_name:
            os.makedirs(folder_name, exist_ok=True)
            return f"Folder '{folder_name}' created"
        else:
            return "Please provide a folder name"

    elif "exit" in cmd or "quit" in cmd:
        return "exit"

    else:
        return None  # not a system command

def main():
    speak("Jarvis online. Waiting for wake word.")

    # Wait for initial wake word
    wait_for_wakeword()
    speak("Yes, I am listening. You can speak your commands now.")
    time.sleep(0.2)

    while True:
        # Listen continuously for commands
        command = listen(duration=6)
        if not command:
            continue  # skip empty recordings

        # UTF-8 safe
        safe_command = command.encode('utf-8', errors='ignore').decode()
        print("You:", safe_command)

        # Check for system commands
        system_response = run_command(command)
        if system_response:
            if system_response == "exit":
                speak("Shutting down. Goodbye.")
                break
            else:
                speak(system_response)
                continue

        # Otherwise, query Ollama AI
        response = ask_ai(command)
        safe_response = response.encode('utf-8', errors='ignore').decode()
        print("Jarvis:", safe_response)
        speak(safe_response)

if __name__ == "__main__":
    main()
