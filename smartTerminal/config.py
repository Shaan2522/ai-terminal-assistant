import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

CONFIG_PATH = Path.home() / ".smartcli"
ENV_FILE = CONFIG_PATH / ".env"

def get_api_key():
    """Load the API key from .env file."""
    if ENV_FILE.exists():
        load_dotenv(ENV_FILE)
        return os.getenv("GEMINI_API_KEY")
    return None

def save_api_key(key: str):
    """Save the API key to .env file."""
    CONFIG_PATH.mkdir(parents=True, exist_ok=True)
    with open(ENV_FILE, "w") as f:
        f.write(f"GEMINI_API_KEY={key.strip()}\n")

def is_api_key_valid(key: str) -> bool:
    """Check if the provided Gemini API key is valid by making a test call."""
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel("gemini-pro")
        # Test with a harmless prompt
        _ = model.generate_content("Hello")
        return True
    except Exception:
        return False

def ensure_valid_api_key() -> str:
    """Ensure a valid API key exists. If not, prompt user until it is valid."""
    key = get_api_key()
    while not key or not is_api_key_valid(key):
        print("❌ Invalid or missing Gemini API key.")
        key = input("🔐 Enter your Gemini API key: ").strip()
        if is_api_key_valid(key):
            save_api_key(key)
        else:
            print("⚠️ That key didn't work. Please try again.\n")
    return key
