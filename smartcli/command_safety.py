def is_dangerous(cmd: str) -> bool:
    danger_patterns = [
        "rm -rf /",
        "mkfs",       # format disk
        ":(){ :|:& };:",  # fork bomb
        "dd if=",     # raw disk overwrite
        "shutdown", "reboot",
        ">:",
    ]
    return any(d in cmd for d in danger_patterns)
