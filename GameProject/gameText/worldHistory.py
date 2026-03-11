import random
import sys
import time

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def world_history():
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    lines = [
        f"Long ago, in the realm known as {CYAN}{BOLD}Ivory{RESET}, the world was a place of peace and prosperity.",
        "Humans, elves, and dwarves lived side by side, under the protection of both magic and steel.",
        "The gods themselves smiled upon this land, and all seemed well.",
        f"But the {RED}{BOLD}peace{RESET} would not last.",
        f"One fateful night, the heavens themselves {YELLOW}{BOLD}broke{RESET} open, and falling stars rained down upon the earth.",
        f"Massive craters, known as {MAGENTA}{BOLD}Sanctuaries{RESET}, were carved into the land, their deep scars burning with an unnatural, malevolent energy.",
        "At first, the kingdoms believed the stars to be a gift from the gods, a divine blessing that would bring new power to the world.",
        f"But the truth was far {RED}{BOLD}darker{RESET}.",
        f"Years later, the Sanctuaries split open—and from within emerged {RED}{BOLD}demons{RESET}, twisted beings of destruction, their eyes burning with rage.",
        "The creatures were immune to mortal weapons and capable of terrible feats of magic.",
        "Entire kingdoms fell in a matter of days, their armies slaughtered and cities reduced to ash.",
        f"With the rise of the Demon Queen, {MAGENTA}{BOLD}Lilith{RESET}, the true scope of the calamity became clear.",
        "The demons were not mindless beasts—they were led by a being of intelligence and malice, a force that had set this chain of destruction in motion.",
        f"Lilith, the demons' mother and creator, sought to {RED}{BOLD}reshape{RESET} the world in her image.",
        "The remnants of humanity, elves, and dwarves fled to the safety of massive fortress cities, built to withstand the onslaught of Lilith’s forces.",
        "But even behind their walls, they were not safe.",
        f"The demons grew in number and power, slowly creeping across the land.",
        f"{GREEN}{BOLD}Hope{RESET} came in an unexpected form.",
        "It was discovered that the fragments left behind by fallen demons could be used by mortals.",
        f"These fragments contained {BLUE}{BOLD}spiritual power{RESET}, granting those who wielded them the strength to fight back.",
        f"These warriors, known as {CYAN}{BOLD}Hunters{RESET}, were the last hope for the world.",
        "They hunted demons, absorbing the fragments they left behind, growing stronger with each battle.",
        f"Yet, even as the Hunters rose to challenge the darkness, a greater threat {YELLOW}{BOLD}loomed{RESET}.",
        "The fragments were not without their price.",
        f"Some Hunters fell to {RED}{BOLD}corruption{RESET}, becoming twisted reflections of the very demons they fought.",
        f"The more they absorbed, the closer they came to becoming the monsters they sought to destroy.",
        f"As the world teetered on the edge of {RED}{BOLD}annihilation{RESET}, a new generation of Hunters appeared.",
        f"You, the {GREEN}{BOLD}Traveler{RESET}, are among them."
    ]

    for line in lines:
        type_text(line)
        time.sleep(0.3)  # faster delay for long intro