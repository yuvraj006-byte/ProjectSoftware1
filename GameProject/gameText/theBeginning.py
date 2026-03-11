def the_beginning():
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    lines = [
        f"The scent of {YELLOW}{BOLD}leather{RESET} and iron fills the air as you step onto unfamiliar soil.",
        f"A vast sky stretches above you—{CYAN}{BOLD}endless{RESET}, like a canvas painted in hues of twilight.",
        f"The horizon is marred by a dark scar—an immense {MAGENTA}{BOLD}Sanctuary{RESET}, the remnants of a star that fell from the heavens.",
        f"The air around you hums with a quiet, oppressive {RED}{BOLD}energy{RESET}, as if the very land mourns the curse that now spreads across it.",
        f"You’ve traveled far, across countless {BLUE}{BOLD}worlds{RESET}, each one leaving its mark.",
        f"From the endless deserts of wind-swept plains to the fractured ruins of shattered cities, each journey was a {YELLOW}{BOLD}lesson{RESET}.",
        f"But this world... {CYAN}{BOLD}Ivory{RESET}... is different.",
        f"The winds here carry the whispers of ancient {MAGENTA}{BOLD}gods{RESET}, the screams of the fallen, and the echoes of battles fought long before your arrival.",
        f"It is a world on the edge of {RED}{BOLD}destruction{RESET}, where humanity clings to the remnants of light.",
        f"A {GREEN}{BOLD}Hunter{RESET}, you’ve come to understand this path—this eternal struggle.",
        f"You’ve crossed realms, seeking {BLUE}{BOLD}power{RESET}, seeking answers, seeking purpose.",
        f"Ivory is but one of the many worlds you must {CYAN}{BOLD}navigate{RESET}.",
        "",
        f"As you step closer to the {YELLOW}{BOLD}fortress{RESET}, the stablemaster eyes you up.",
        f'He mutters: "{RED}{BOLD}Another Hunter{RESET}, hm? You think you’ll find strength here?"',
        f'"You’ll find nothing but {RED}{BOLD}death{RESET}. But that\'s the way of things, isn\'t it?"',
        f'"A Hunter only ever survives for one reason... to fight the {MAGENTA}{BOLD}darkness{RESET}."',
        f'"Try not to {YELLOW}{BOLD}die{RESET} on your first flight."',
        "",
        f"The world of {CYAN}{BOLD}Ivory{RESET} welcomes you.",
        f"But whether you will {GREEN}{BOLD}rise{RESET} above its destruction... or be {RED}{BOLD}consumed{RESET} by it...",
        f"That is yet to be {MAGENTA}{BOLD}written{RESET}."
    ]

    for line in lines:
        print(line)