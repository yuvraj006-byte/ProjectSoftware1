import sys
import time

def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


class Color:
    CYAN           = "\033[1;36m"
    YELLOW         = "\033[1;33m"
    GREEN          = "\033[1;32m"
    MAGENTA        = "\033[1;35m"
    BRIGHT_BLACK   = "\033[1;30m"
    RED            = "\033[1;31m"
    RESET          = "\033[0m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

def butler_player_death():
    print(f"\n{c('🎩 Butler:', Color.CYAN)}")

    lines = [
        "Alas, sir… you have fallen in battle.",
        "Do not despair — one can always try again.",
        f"I advise you to {c('rest', Color.GREEN)}, take on {c('quests', Color.MAGENTA)}, or {c('train', Color.YELLOW)} to prepare for your next challenge.",
        "Remember, every defeat is a lesson in disguise."
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)