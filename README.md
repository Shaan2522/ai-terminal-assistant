# NL-termiNL 🧠💻 – natural language terminal

**NL-termiNL** is an AI-powered smart shell interface that allows you to run terminal commands using natural language. No need to remember complex syntax — just describe what you want, and it figures out the command for you.

> 🤖 Powered by Gemini AI  
> 🐧 Works on Linux and Windows  
> 🧠 Understands everyday language  
> 🔒 Detects and warns against dangerous commands

---

## ✨ Features

- 🔍 Understands plain English: `show files modified today`
- 🧠 Translates using Gemini (`gemini-2.5-flash` model)
- 🛡️ Filters dangerous or destructive commands
- ⚙️ Automatically executes safe commands
- 💾 Saves command history for auto-suggestions
- 🖥️ Cross-platform: works on both **Linux** and **Windows**

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
[git clone https://github.com/Shaan2522/ai-terminal-assistant.git](https://github.com/Shaan2522/ai-terminal-assistant.git)
```

### 2. Install Requirements

```
pip install -r requirements.txt
```

### 3. Run It

```
cd smartTerminal
python main.py
```

You'll see a smart shell interface:

## 🔐 Set Your Gemini API Key
On first run, you'll be prompted to enter your Gemini API key.

The key will be securely saved to ~/.smartTerminal/.env.

```
🔮 NL-termiNL Shell. Type 'help' or natural language commands.
NL-termiNL> show files modified today
🧠 Translating...
💡 Translated: forfiles /p . /d +0 /c "cmd /c echo @file"

"ai_translator.py"
"command_safety.py"
"config.py"
"history.txt"
"main.py"
"shell.py"
"__pycache__"
```

If it's a safe command, it runs automatically.
If it's dangerous (e.g. ```rm -rf /```), you'll get a safety warning before execution.

## 📁 Project Structure

```
ShellPilot/
├── smartTerminal/                 # Core Python package
│   ├── main.py                    # Entry point
│   ├── shell.py                   # Shell loop and logic
│   ├── ai_translator.py           # Gemini integration
│   ├── command_safety.py          # Dangerous command filter
│   ├── config.py                  # API key handling
│   └── history.txt                # User command history
├── .gitignore
├── README.md
├── requirements.txt
```

## 📄 License
This project is licensed under the MIT License — use it, modify it, share it freely.
