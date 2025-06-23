import subprocess
import os
import shutil
import platform
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from ai_translator import translate_to_command
from command_safety import is_dangerous
from config import get_api_key, save_api_key

HISTORY_FILE = "history.txt"

class SmartShell:
    def __init__(self):
        self.session = PromptSession()
        self.load_history()
        self.ensure_api_key()

    def ensure_api_key(self):
        if not get_api_key():
            print("🔑 Gemini API key not found.")
            key = input("Please enter your Gemini API key: ").strip()
            if key:
                save_api_key(key)
                print("✅ API key saved.")
            else:
                print("❌ Cannot proceed without API key.")
                exit(1)

    def load_history(self):
        self.history = []
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE) as f:
                self.history = [line.strip() for line in f.readlines()]
        self.completer = WordCompleter(self.history, ignore_case=True)

    def save_to_history(self, command):
        if command not in self.history:
            self.history.append(command)
            with open(HISTORY_FILE, "a") as f:
                f.write(command + "\n")
        self.completer = WordCompleter(self.history, ignore_case=True)

    def is_likely_shell_command(self, text):
        if text.startswith("./") or text.split()[0] in self.history:
            return True
        binary = shutil.which(text.split()[0])
        return binary is not None

    def run(self):
        print("🔮 NL-termiNL Shell. Type commands or natural language.")
        while True:
            try:
                text = self.session.prompt("NL-termiNL> ", completer=self.completer)
                if not text.strip():
                    continue

                if text.strip().lower() in {"exit", "quit"}:
                    break

                original_text = text.strip()

                if not self.is_likely_shell_command(original_text):
                    print("🧠 Translating...")
                    text = translate_to_command(original_text).strip()
                    print(f"💡 Translated: {text}")

                if is_dangerous(text):
                    confirm = input("⚠️ Dangerous command detected. Proceed? (y/N): ")
                    if confirm.lower() != 'y':
                        continue

                self.save_to_history(text)
                subprocess.run(text, shell=True)

            except KeyboardInterrupt:
                continue
            except EOFError:
                break
        print("👋 Exiting NL-termiNL")
