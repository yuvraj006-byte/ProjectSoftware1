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
    sys.stdout.write("\n")

# Butler dialogue for first demonic spirit
def butler_first_demonic_spirit():
    lines = [
        f'{c("🎩 Butler:", Color.CYAN)} "Master, it is time for your first companion in battle."',
        f'"You shall receive a {c("demonic spirit", Color.RED)} — it may manifest as a {c("weapon", Color.YELLOW)} or {c("armor", Color.GREEN)}."',
        f'"This spirit will aid you in fighting the demons that roam these lands."',
        f'"However, beware… its {c("core", Color.MAGENTA)} is demonic in nature."',
        f'"Prolonged use could {c("corrupt", Color.RED)} your soul if you are not careful."',
        f'"Use it wisely, Master, and let it be a tool, not your master."'
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)