import os
from pathlib import Path
from dotenv import load_dotenv

CONFIG_PATH = Path.home() / ".smartcli"
ENV_FILE = CONFIG_PATH / ".env"

def get_api_key():
    load_dotenv(ENV_FILE)
    return os.getenv("GEMINI_API_KEY")

def save_api_key(key: str):
    CONFIG_PATH.mkdir(parents=True, exist_ok=True)
    with open(ENV_FILE, "w") as f:
        f.write(f"GEMINI_API_KEY={key.strip()}\n")
