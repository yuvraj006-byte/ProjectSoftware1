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

# Color helper
def c(text, color):
    return f"{color}{text}{Color.RESET}"

# Typewriter effect
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# Dramatic response for invalid Butler input
def butler_invalid_choice():
    lines = [
        f"The summoning was performed, yet the words you spoke faltered...",
        f"The {c('Butler', Color.CYAN)}'s gaze pierces through your hesitation,",
        f"A {c('silence', Color.MAGENTA)} fills the air, heavy and accusing.",
        f"Even the {c('shadows', Color.RED)} recoil from your inability to ask with clarity.",
        f"Choose wisely next time, Master, lest your errors linger in the {c('void', Color.BLUE)}."
    ]
    
    for line in lines:
        type_text(line, speed=0.04)
        time.sleep(0.3)