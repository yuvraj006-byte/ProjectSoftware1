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


def butler_intro():

    lines = [
        f"Excellent. Your {c('name', Color.GREEN)} has been properly recorded.",
        "Allow me to introduce myself.",
        f"My name is {c('Alfred', Color.CYAN)}.",
        f"I am your butler and {c('advisor', Color.YELLOW)}.",
        "I will assist you throughout your adventure.",
        f"Before we begin, I recommend reviewing the {c('history of this world', Color.MAGENTA)}.",
        f"Understanding the {c('past', Color.MAGENTA)} may prove useful."
    ]

    print(f"\n{c('🎩 Butler:', Color.CYAN)}")

    for line in lines:
        type_text(line)
        time.sleep(0.3)

    type_text(f"\nType {c('History', Color.YELLOW)} to read the world history (Type {c('No', Color.RED)} to not read the {c('History', Color.YELLOW)}!).")