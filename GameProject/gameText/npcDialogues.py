import sys
import time

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class Color:
    RESET = "\033[0m"
    
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    
    BOLD = "\033[1m"


def total_dialogues():

    def print_with_delay(lines):
        print()
        for line in lines:
            type_text(line)
            time.sleep(0.5)
        print()

    def dialogue_1():
        return [
            "They fell like salvation.",
            f"Burning stars tearing the sky open. Priests called it {Color.YELLOW}divine fire{Color.RESET}.",
            f"{Color.RED}Fools.{Color.RESET}",
            "Years later, the craters cracked… and something inside them started breathing.",
            f"That metal you carry? Came from their {Color.CYAN}bones{Color.RESET}.",
            "You want power? Fly into one.",
            f"You want to live? {Color.BOLD}Don’t go too deep.{Color.RESET}"
        ]

    def dialogue_2():
        return [
            f"They don’t fear {Color.RED}pain{Color.RESET}.",
            f"Steel passes through them like mist unless it’s {Color.CYAN}Sanctuary-forged{Color.RESET}.",
            "Cut one down and it leaves a fragment behind.",
            "That glow you feel when you absorb it?",
            "That’s their world clinging to yours.",
            "Don’t take too many without resting.",
            f"Hunters who do start hearing {Color.MAGENTA}whispers{Color.RESET}."
        ]

    def dialogue_3():
        return [
            "The Stablemaster goes quiet.",
            "We don’t speak her name loudly.",
            f"The demons call her {Color.RED}{Color.BOLD}Mother{Color.RESET}.",
            "Some say she didn’t arrive with the stars.",
            "Some say she sent them.",
            "If you ever stand before her…",
            "You won’t be fighting a beast.",
            "You’ll be fighting a will older than kingdoms."
        ]

    def dialogue_4():
        return [
            "You’re not the first.",
            "Won’t be the last.",
            "Some chase gold.",
            "Some chase revenge.",
            f"The smart ones chase {Color.GREEN}strength{Color.RESET}.",
            "Every fragment you absorb makes you less human… and more capable of killing what isn’t.",
            "He studies you carefully.",
            "Question is — how much of yourself are you willing to trade?"
        ]

    def dialogue_if_leave():
        return [
            "Try not to die out there.",
            f"The sky’s crowded enough with {Color.CYAN}ghosts{Color.RESET}."
        ]

    def talk_to_stablemaster():
        options = [
            "1. Ask about the Sanctuaries",
            "2. Ask about the Demons",
            "3. Ask about Lilith",
            "4. Ask about Hunters",
            "5. Leave"
        ]

        print()
        for option in options:
            print(option)

        while True:
            choice = input("\nWHAT WILL YOU DO? (1/2/3/4/5): ")

            if choice == "1":
                print_with_delay(dialogue_1())
                break
            elif choice == "2":
                print_with_delay(dialogue_2())
                break
            elif choice == "3":
                print_with_delay(dialogue_3())
                break
            elif choice == "4":
                print_with_delay(dialogue_4())
                break
            elif choice == "5":
                print_with_delay(dialogue_if_leave())
                break
            else:
                print("INVALID CHOICE! PLEASE CHOOSE A NUMBER BETWEEN 1-5.")

    talk_to_stablemaster()