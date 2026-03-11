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

import time

def butler_new_game():

    lines = [
        f'"Welcome, Master. It seems you have chosen to begin a {c("new journey", Color.GREEN)}."',
        f'"From this moment forward, your story in this world begins."',
        f'"The roads you take, the battles you fight, and the choices you make will shape your fate."',
        f'"Whenever you wish to act, simply open the {c("Menu", Color.YELLOW)}."',
        f'"It will present the paths available to you in this world."',
        f'"Take your time, Master... every great legend begins with a single step."'
    ]

    print(f"\n{c('🎩 Butler:', Color.CYAN)}")

    for line in lines:
        print(line)
        time.sleep(0.3)