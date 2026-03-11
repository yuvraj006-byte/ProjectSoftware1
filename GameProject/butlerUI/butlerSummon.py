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

# Summon Butler dialogue
def butler_summon():
    lines = [
        f'{c("🎩 Butler:", Color.CYAN)} "At your command, Master... I have arrived."',
        f'"I stand ready to offer guidance, advice, and assistance in your {c("adventure", Color.GREEN)}."',
        f'"Whether it be {c("quests", Color.MAGENTA)}, {c("travel", Color.YELLOW)}, or facing {c("dangerous foes", Color.RED)}, I shall be your constant companion."',
        f'"Consult me whenever you require wisdom, Master."',
        f'"Your journey begins anew, and I shall see you through its perils."'
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)