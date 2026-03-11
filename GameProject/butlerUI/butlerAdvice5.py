import sys
import time

# Color class
class Color:
    CYAN         = "\033[1;36m"
    YELLOW       = "\033[1;33m"
    GREEN        = "\033[1;32m"
    MAGENTA      = "\033[1;35m"
    BRIGHT_BLACK = "\033[1;30m"
    RED          = "\033[1;31m"
    RESET        = "\033[0m"

# Color helper
def c(text, color):
    return f"{color}{text}{Color.RESET}"

# Typewriter effect
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Butler dialogue for choosing an empire
def butler_choose_empire():
    lines = [
        f'{c("🎩 Butler:", Color.CYAN)} "Master, before you embark on your adventure, a crucial choice awaits."',
        f'"You must select an {c("empire", Color.YELLOW)} to serve as your starting point."',
        f'"Each empire offers unique advantages, resources, and challenges."',
        f'"Choose wisely, for this decision will shape the beginning of your journey."',
        f'"Once you have made your choice, the {c("Menu", Color.MAGENTA)} will guide you to your first actions."'
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)
