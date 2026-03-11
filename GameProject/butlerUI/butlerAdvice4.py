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

def butler_after_history():

    lines = [
        f'"Ah, I see that you are now acquainted with the {c("World History", Color.MAGENTA)}, Master."',
        f'"Understanding the past is the first step to surviving the future."',
        f'"Now the real journey begins."',
        f'"You may {c("start a new adventure", Color.GREEN)} and forge your own legend..."',
        f'"...or {c("load a previous save", Color.YELLOW)} if you have unfinished business."',
        f'"Choose wisely, Master. The fate of this world may depend on it."'
    ]

    print(f"\n{c('🎩 Butler:', Color.CYAN)}")

    for line in lines:
        type_text(line)
        time.sleep(0.3)
