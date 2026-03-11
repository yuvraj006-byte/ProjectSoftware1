import random
import sys
import time

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


class Color:
    RED = "\033[91m"
    DARK_RED = "\033[31m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    

def forest_scene_1():
    return (
        f"The {Color.GREEN}trees{Color.RESET} grow too close together.",
        f"Light barely touches the {Color.YELLOW}forest floor{Color.RESET}.",
        f"{Color.DIM}Branches{Color.RESET} creak without wind.",
        f"Something {Color.MAGENTA}shifts{Color.RESET} between the {Color.GREEN}trunks{Color.RESET}."
    )

def forest_scene_2():
    return (
        f"{Color.DARK_RED}Claw marks{Color.RESET} carve deep into the bark.",
        f"The ground is disturbed — recently.",
        f"A metallic scent lingers in the air.",
        f"You are being {Color.RED}{Color.BOLD}tracked{Color.RESET}."
    )

def forest_scene_3():
    return (
        f"The birds fall silent.",
        f"Even the insects stop.",
        f"Your {Color.CYAN}shadow{Color.RESET} stretches unnaturally long.",
        f"A {Color.RED}{Color.BOLD}demon{Color.RESET} steps into view."
    )

# ============================================================================================================================

def dungeon_scene_1():
    return (
        f"{Color.CYAN}Cold air{Color.RESET} rises from the {Color.DIM}stone staircase{Color.RESET}.",
        f"{Color.DIM}Moisture{Color.RESET} drips from the ceiling.",
        f"Old {Color.YELLOW}chains{Color.RESET} sway in the {Color.DIM}darkness{Color.RESET}.",
        f"Something {Color.MAGENTA}breathes{Color.RESET} below."
    )

def dungeon_scene_2():
    return (
        f"Faded symbols cover the walls.",
        f"{Color.DIM}Broken weapons{Color.RESET} litter the floor.",
        f"A distant {Color.RED}{Color.BOLD}scream{Color.RESET} echoes.",
        f"It ends abruptly."
    )

# ============================================================================================================================

def demon_nest_scene_1():
    return (
        f"The smell of {Color.GREEN}rot{Color.RESET} overwhelms you.",
        f"{Color.DIM}Bones{Color.RESET} crunch beneath your {Color.YELLOW}boots{Color.RESET}.",
        f"The {Color.RED}ground{Color.RESET} pulses faintly.",
        f"You’ve found their {Color.MAGENTA}{Color.BOLD}nest{Color.RESET}."
    )

def demon_nest_scene_2():
    return (
        f"{Color.YELLOW}{Color.BOLD}Red eyes{Color.RESET} blink open in the dark.",
        f"Low growls surround you.",
        f"The walls seem to move.",
        f"They were waiting."
    )

# ============================================================================================================================

def corruption_zone_scene():
    return (
        f"The earth here is {Color.DIM}blackened{Color.RESET} and cracked.",
        f"No life stirs in this place.",
        f"Your weapon hums with tension.",
        f"Something {Color.MAGENTA}powerful{Color.RESET} watches."
    )


def fog_forest_scene():
    return (
        f"Thick mist coils around your legs.",
        f"The path behind you vanishes.",
        f"{Color.CYAN}Footsteps{Color.RESET} echo beside yours.",
        f"You are no longer alone."
    )


def ancient_prison_scene():
    return (
        f"{Color.DIM}Rust-eaten bars{Color.RESET} line the corridor.",
        f"Most cells are empty.",
        f"One is not.",
        f"The door creaks open slowly."
    )

# ============================================================================================================================


environments_list = [
    forest_scene_1, forest_scene_2, forest_scene_3,
    dungeon_scene_1, dungeon_scene_2,
    corruption_zone_scene, fog_forest_scene, ancient_prison_scene
]

environments_pool = environments_list[:]
random.shuffle(environments_pool) 

def environments_output():
    global environments_pool
    
    if not environments_pool:
        environments_pool = environments_list[:]
        random.shuffle(environments_pool)
    
    scene_function = environments_pool.pop()
    scene_lines = scene_function()  
    
    for line in scene_lines:
        type_text(line)
        time.sleep(0.5)

    time.sleep(1)