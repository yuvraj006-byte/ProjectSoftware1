import sys
import time

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def boss_defeated():
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    ending_text = [
        f"{CYAN}Victory is yours.{RESET}",
        f"{YELLOW}But not complete.{RESET}",
        f"{RED}One final shadow remains.{RESET}",
        f"{CYAN}The story continues...{RESET}"
    ]

    for line in ending_text:
        type_text(line)
        time.sleep(1) 