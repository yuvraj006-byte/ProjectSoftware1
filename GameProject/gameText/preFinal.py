import sys
import time

def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def pre_final():
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    lines = [
        f"You stand at the gates of Lucifer's capital, a fortress of {MAGENTA}{BOLD}black stone{RESET} and demon flesh.",
        f"The air reeks of {RED}{BOLD}death{RESET}.",
        f"The rivers boil with {GREEN}{BOLD}corruption{RESET}, churning with sickly miasma.",
        f"The world itself is {RED}{BOLD}dying{RESET} beneath Lucifer's influence.",
        f"A man, barely clinging to {CYAN}{BOLD}life{RESET}, stumbles toward you.",
        f"His skin is cracked, his blood {RED}{BOLD}dripping{RESET} from trembling fingers.",
        f"“She {YELLOW}{BOLD}waits{RESET}... The end is near...”",
        f"“If you fail, all will be {RED}{BOLD}lost{RESET}.”",
        f"The ground beneath you begins to {MAGENTA}{BOLD}writhe{RESET}.",
        f"The whispers of the {BLUE}{BOLD}damned{RESET} ride the wind.",
        f"Through smoke and ruin, {RED}{BOLD}Lilith{RESET} appears.",
        f"Her silhouette towers against the corrupted {CYAN}{BOLD}sky{RESET}.",
        f"“So the little {YELLOW}{BOLD}Hunter{RESET} finally arrives.”",
        f"“Do you think you can stop me, child of my {MAGENTA}{BOLD}fragments{RESET}?”",
        f"Her laughter {RED}{BOLD}echoes{RESET} across the wasteland.",
        f"The {GREEN}{BOLD}choice{RESET} you make now will decide everything.",
        f"Whether the world will {RED}{BOLD}burn{RESET}… or be saved."
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)