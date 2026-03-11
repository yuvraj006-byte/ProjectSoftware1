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

def butler_travel_advice(player_gold, travel_cost):

    print(f"\n{c('🎩 Butler:', Color.CYAN)}")

    if player_gold >= travel_cost:
        # Player has enough gold
        lines = [
            f"Traveling to another location will cost you {c(f'{travel_cost} gold', Color.YELLOW)}.",
            "Make sure you really need to go, sir. Travel can be dangerous and costly."
        ]
    else:
        # Player does not have enough gold
        lines = [
            f"You only have {c(f'{player_gold} gold', Color.RED)}, which is not enough to travel.",
            f"I advise you to go on an {c('adventure', Color.GREEN)} or complete some {c('quests', Color.MAGENTA)} to earn more gold before traveling."
        ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)