import random
import time 

def opening_scene():
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    lines = [
        f"You stand at the edge of a ruined {YELLOW}{BOLD}stronghold{RESET}, gazing across a world ravaged by demons.",
        f"Smoke rises from distant villages, and twisted {MAGENTA}{BOLD}shadows{RESET} move in the forests.",
        f"The air smells of burnt earth, the faint cries of the {RED}{BOLD}dying{RESET} echo from across the plains.",
        f"Suddenly, you notice a figure kneeling beside a charred {CYAN}{BOLD}body{RESET}—an old man, covered in blood, trembling in pain.",
        f"Through ragged breath, he murmurs of {RED}{BOLD}Lilith{RESET} and the strength she gains each day.",
        f'“There\'s no {RED}{BOLD}hope{RESET} left. We... we thought we could fight. We were wrong...”',
        f"His words hang in the air, heavy with {YELLOW}{BOLD}grief{RESET}.",
        f"You feel the pulse of your {MAGENTA}{BOLD}Demonic Spirit{RESET} fragment thrumming in your chest.",
        f"A grim reminder that you are bound to this {RED}{BOLD}darkness{RESET}.",
        f"“The world survives in {CYAN}{BOLD}fragments{RESET}.”",
        f"“You are the {GREEN}{BOLD}light{RESET} that remains.”",
        f"“{YELLOW}{BOLD}Hunt{RESET}. Fight. Survive... and confront the one who began it all.”",
        f"With {BLUE}{BOLD}resolve{RESET} hardening in your heart, you turn away from the broken figure.",
        f"You step forward.",
        f"The first {MAGENTA}{BOLD}mission{RESET} begins."
    ]

    for line in lines:
        print(line)
        time.sleep(random.uniform(0.3, 0.6))