import sys
import time

# ---------------- Colors ----------------
class Color:
    CYAN         = "\033[1;36m"
    YELLOW       = "\033[1;33m"
    GREEN        = "\033[1;32m"
    MAGENTA      = "\033[1;35m"
    BRIGHT_BLACK = "\033[1;30m"
    RED          = "\033[1;31m"
    BOLD         = "\033[1m"
    RESET        = "\033[0m"

# ---------------- Helpers ----------------
def c(text, color):
    return f"{color}{text}{Color.RESET}"

def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

    
# Player logs off with save
def goodbye_saved(save_id):
    lines = [
        f"{Color.CYAN}{Color.BOLD}🎩 Butler: {Color.RESET} Master, your progress has been {c('Safely', Color.GREEN)} recorded.",
        f"Take your rest, and return when you are ready for further adventures.",
        f"I shall await your {c('command', Color.MAGENTA)}, as always.",
        f"{c('Farewell', Color.YELLOW)} for now, Master.",
        f"Your Save ID is {c({save_id}, Color.RED)}.",
        f"You Must Remember This."
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)  # pause between lines

# Player tries to exit without saving
def warn_unsaved():
    lines = [
        f"{Color.CYAN}{Color.BOLD}🎩 Butler: {Color.RESET} Master, it seems you are about to leave without saving.",
        f"Your progress could be {c('lost', Color.RED)} if you proceed.",
        f"I strongly advise you to {c('save', Color.YELLOW)} your game before taking your leave.",
        f"Do not let careless haste undo your efforts."
    ]
    for line in lines:
        type_text(line)
        time.sleep(0.3)  # pause between lines    