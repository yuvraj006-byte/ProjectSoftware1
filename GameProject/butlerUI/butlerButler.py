import sys
import time

# Color class
class Color:
    RED       = "\033[91m"
    MAGENTA   = "\033[95m"
    CYAN      = "\033[96m"
    YELLOW    = "\033[93m"
    GREEN     = "\033[92m"
    BLUE      = "\033[94m"
    BOLD      = "\033[1m"
    RESET     = "\033[0m"

# Typewriter effect
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# ---------------- WHO IS THE BUTLER ----------------
def who_is_butler():
    lines = [
        f"{Color.CYAN}{Color.BOLD}🎩 Butler:{Color.RESET} I am neither fully of this world nor the next…",
        f"My eyes see what you cannot, and my whispers trace paths best left untaken.",
        f"Some call me guide, others call me shadow… but names mean little here.",
        f"I have watched many Masters rise, and many more {Color.RED}{Color.BOLD}fall{Color.RESET}.",
        f"Do not seek to understand me, Master… it is safer to heed my words."
    ]
    
    for line in lines:
        type_text(line)
        time.sleep(0.8)

# ---------------- BUTLER'S ROLE ----------------
def butler_role():
    lines = [
        f"{Color.CYAN}{Color.BOLD}🎩 Butler:{Color.RESET} My purpose is... fluid, much like the {Color.MAGENTA}dark currents{Color.RESET} between worlds.",
        f"I am here to {Color.YELLOW}{Color.BOLD}guide{Color.RESET}, to warn, and occasionally to judge.",
        f"I will speak truths you may not wish to hear, and secrets that may haunt your dreams.",
        f"Do not mistake my presence for mercy—every choice you make echoes beyond your understanding.",
        f"Follow my voice, Master, or be consumed by the {Color.RED}{Color.BOLD}shadows{Color.RESET} that linger ever near."
    ]
    
    for line in lines:
        type_text(line)
        time.sleep(0.3)