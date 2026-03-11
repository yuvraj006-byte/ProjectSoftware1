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



def butler_npc_advice():

    lines = [
        f"Now that you are all {c('geared', Color.MAGENTA)} up, it is time to take your first step.",
        f"I suggest you visit the {c('Stable Master', Color.YELLOW)} nearby.",
        f"He may have valuable {c('advice', Color.GREEN)} for your journey ahead.",
        "Pay close attention to what he says — even the smallest hint may prove useful.",
        f"And remember, {c('patience', Color.CYAN)} can be just as important as courage."
    ]

    print(f"\n{c('🎩 Butler:', Color.CYAN)}")

    for line in lines:
        type_text(line)
        time.sleep(0.3)