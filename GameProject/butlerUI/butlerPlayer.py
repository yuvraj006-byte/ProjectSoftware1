import sys
import time

# Color class
class Color:
    RED       = "\033[91m"
    MAGENTA   = "\033[95m"
    CYAN      = "\033[96m"
    YELLOW    = "\033[93m"
    GREEN     = "\033[92m"
    BLUE      = "\033[94m"
    BOLD      = "\033[1m"
    RESET     = "\033[0m"

# Typewriter effect
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ---------------- WHO PLAYER IS ----------------
def who_player():
    lines = [
        f"{Color.CYAN}{Color.BOLD}🎩 Butler:{Color.RESET} You are a {Color.CYAN}{Color.BOLD}traveler{Color.RESET} between worlds, a being who has journeyed through countless realms, seeking strength and purpose.",
        f"Every world you visit leaves its {Color.YELLOW}{Color.BOLD}mark{Color.RESET} upon you, shaping you into a Hunter—a warrior whose path is defined by the hunt for power, and ultimately, the fight to save or destroy entire worlds.",
        f"Your arrival in {Color.CYAN}{Color.BOLD}Ivory{Color.RESET} marks a new chapter in your journey.",
        f"You are not the first to visit this world—many before you have fought and {Color.RED}{Color.BOLD}fallen{Color.RESET}.",
        f"But the ancient history of Ivory calls to you, as the {Color.MAGENTA}{Color.BOLD}Sanctuaries{Color.RESET} pulse with power, and the whispers of {Color.RED}{Color.BOLD}Lilith{Color.RESET} stir in the shadows.",
        f"You are not alone in this world, but you are {Color.YELLOW}{Color.BOLD}isolated{Color.RESET} in your quest.",
        f"The Hunters you encounter may be {Color.GREEN}{Color.BOLD}allies{Color.RESET} one moment, and enemies the next."
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)

# ---------------- PLAYER ROLE ----------------
def player_role():
    lines = [
        f"{Color.CYAN}{Color.BOLD}🎩 Butler:{Color.RESET}: The Demonic Spirits you absorb, though granting you {Color.BLUE}{Color.BOLD}power{Color.RESET}, may come to consume you, turning you into the very thing you are trying to destroy.",
        f"This world is falling apart—and it needs someone to {Color.CYAN}{Color.BOLD}decide{Color.RESET} whether it will be saved or consumed.",
        f"The final {Color.MAGENTA}{Color.BOLD}confrontation{Color.RESET} awaits.",
        f"But how you get there, and what you become along the way, will be determined by your {Color.YELLOW}{Color.BOLD}actions{Color.RESET}.",
        f"Will you become the new {Color.GREEN}{Color.BOLD}ruler{Color.RESET} of this decaying world, the one who brings it to order under a new reign?",
        f"Or will you choose to {Color.RED}{Color.BOLD}destroy{Color.RESET} all fragments, ending Lilith's influence once and for all, even if it means the world will collapse?",
        f"The {Color.CYAN}{Color.BOLD}choice{Color.RESET} is yours."
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)