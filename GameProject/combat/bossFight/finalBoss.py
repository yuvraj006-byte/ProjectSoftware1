def final_boss():
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    lines = [
        f"At the summit of the central {MAGENTA}{BOLD}Sanctuary{RESET}, you stand before {RED}{BOLD}Lucifer{RESET}.",
        f"His presence radiates terrible {YELLOW}{BOLD}majesty{RESET}, bending air and fracturing the sky.",
        f"Shadows coil at his feet like living {CYAN}{BOLD}things{RESET}.",
        f"Every breath tastes of ash and {BLUE}{BOLD}starlight{RESET}.",
        f"His wings unfurl in a slow, deliberate {MAGENTA}{BOLD}arc{RESET}.",
        f"His eyes burn with ancient {RED}{BOLD}fire{RESET}.",
        f"“The {CYAN}{BOLD}fragments{RESET} were never yours to claim.”",
        f"“They were shards of my {YELLOW}{BOLD}fall{RESET}… scattered, waiting… returning.”",
        f"You feel the {MAGENTA}{BOLD}truth{RESET} threading through your veins.",
        f"You are {RED}{BOLD}bound{RESET} to him.",
        f"A mirror. A vessel. A {BLUE}{BOLD}consequence{RESET}.",
        f"The {YELLOW}{BOLD}battle{RESET} erupts.",
        f"Light collides with {MAGENTA}{BOLD}shadow{RESET} in cataclysm.",
        f"The fragments blaze within you, answering his {RED}{BOLD}call{RESET}.",
        f"Reality fractures into spirals of fire and {CYAN}{BOLD}void{RESET}.",
        f"In the end, {RED}{BOLD}Lucifer{RESET} falls to one knee.",
        f"His crown lies {YELLOW}{BOLD}shattered{RESET}.",
        f"“Power does not {GREEN}{BOLD}die{RESET},” he murmurs.",
        f"“It {MAGENTA}{BOLD}chooses{RESET}.”",
        "",
        f"Will you {RED}{BOLD}ascend{RESET} and claim dominion?",
        f"Will you {CYAN}{BOLD}destroy{RESET} the fragments and end his legacy?",
        f"Or will you {GREEN}{BOLD}release{RESET} the power back to the cosmos?",
        "",
        f"The world {YELLOW}{BOLD}trembles{RESET}.",
        f"The fate of {CYAN}{BOLD}Open Skies{RESET} rests in your hands."
    ]

    for line in lines:
        print(line)