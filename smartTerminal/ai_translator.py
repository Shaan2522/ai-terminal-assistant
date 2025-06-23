from config import ensure_valid_api_key
import google.generativeai as genai
import os

os_name = os.name  # 'posix' for Linux/macOS, 'nt' for Windows

def translate_to_command(nl_text: str) -> str:
    api_key = ensure_valid_api_key()  # Ensures key exists and is valid

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = (
            f"You are a command-line assistant.\n"
            f"Your job is to convert plain English into an executable {os_name} command.\n"
            "Important rules:\n"
            "- Do NOT use backticks or markdown formatting.\n"
            "- Do NOT explain the command.\n"
            "- Return ONLY the command, nothing else.\n"
            "- Make sure it is safe, common, and minimal.\n\n"
            f"User request: {nl_text}\n"
            "Command:"
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"[❌ Gemini API error: {e}]"
