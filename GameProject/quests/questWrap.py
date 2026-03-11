import time
import random
from datetime import datetime
from tabulate import tabulate
from .easyQuests.questEasy1 import questE1 
from .easyQuests.questEasy2 import questE2
from .easyQuests.questEasy3 import questE3
from .easyQuests.questEasy4 import questE4
from .easyQuests.questEasy5 import questE5
from .hardQuests.questHard1 import questH1
from .hardQuests.questHard2 import questH2
from .hardQuests.questHard3 import questH3
from .hardQuests.questHard4 import questH4
from .hardQuests.questHard5 import questH5
from .hardQuests.questHard6 import questH6
from .hardQuests.questHard7 import questH7
from .hardQuests.questHard8 import questH8
from .hardQuests.questHard9 import questH9
from .hardQuests.questHard10 import questH10
from .mediumQuests.questMedium1 import questM1
from .mediumQuests.questMedium2 import questM2
from .mediumQuests.questMedium3 import questM3
from .mediumQuests.questMedium4 import questM4
from .mediumQuests.questMedium5 import questM5
from .mediumQuests.questMedium6 import questM6
from .mediumQuests.questMedium7 import questM7
from playerUI.levelingUp import process_leveling
from quests.reward.questReward import quest_reward 

class Color:
    CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    GREEN = "\033[1;32m"
    MAGENTA = "\033[1;35m"
    BRIGHT_BLACK = "\033[1;30m"
    RED = "\033[1;31m"
    RESET = "\033[0m"
    BOLD = "\033[1;31m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

def table(title, headers, rows):
    print(f"\n{c(title, Color.MAGENTA)}")
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def pause():
    input('\033[32mPress Enter to continue...\033[0m') 

def full_quest_wrap(conn, save_id, current_region):

    # Map quest IDs to functions
    quest_functions = {
        1: questE1, 2: questE2, 3: questE3, 4: questE4, 5: questE5,
        6: questM1, 7: questM2, 8: questM3, 9: questM4, 10: questM5, 11: questM6, 12: questM7,
        13: questH1, 14: questH2, 15: questH3, 16: questH4, 17: questH5, 18: questH6, 19: questH7,
        20: questH8, 21: questH9, 22: questH10
    }

    cursor = conn.cursor(buffered=True)

    # Fetch quests (only those NOT completed by this save)
    cursor.execute("""
        SELECT quests.id, quests.quest_name, quests.reward_xp, quests.region, quests.city_id
        FROM quests
        WHERE quests.region = %s
        AND NOT EXISTS (
            SELECT 1
            FROM quest_progress qp
            WHERE qp.quest_id = quests.id
            AND qp.save_id = %s
        )
    """, (current_region, save_id))

    results = cursor.fetchall()

    if not results:
        print(f"No available quests. Make sure quests exist in Region: {current_region}")
        return False

    # Display quests
    quest_rows = []

    for i, (quest_id, quest_name, reward_xp, region, city_id) in enumerate(results, 1):
        quest_rows.append([
            c(i, Color.CYAN),
            c(quest_name, Color.GREEN),
            c(reward_xp, Color.YELLOW),
            c(region, Color.MAGENTA),
            c(city_id if city_id else "Global", Color.BRIGHT_BLACK)
        ])

    table(
        "Available Quests",
        ["#", "Quest Name", "Reward XP", "Region", "City"],
        quest_rows
    )
    # Player chooses quest
    while True:
        choice = input("Choose a quest number: ")
        if not choice.isdigit():
            print("Invalid input. Enter a number.")
            continue
        choice = int(choice)
        if 1 <= choice <= len(results):
            break
        else:
            print("Invalid choice. Pick a valid number.")

    selected_quest = results[choice - 1]
    quest_id = selected_quest[0]
    exp_gained = selected_quest[2]

    # Run quest function
    if quest_id not in quest_functions:
        print("Quest function not implemented for ID:", quest_id)
        cursor.close()
        return False

    success = quest_functions[quest_id]()

    if not success:
        print("Quest failed.")
        cursor.close()
        return False

    # Fetch player stats
    cursor.execute("SELECT xp, level, health FROM player_stats WHERE save_id = %s", (save_id,))
    player_data = cursor.fetchone()

    if not player_data:
        print("Player stats not found.")
        cursor.close()
        return False

    current_xp, current_level, current_health = player_data

    # At the very end of full_quest_wrap(), after rewards

    # --- Lore Fragments ---
    lore_fragments = {
        1: f"The falling {Color.YELLOW}{Color.BOLD}stars{Color.RESET} were not {Color.RED}{Color.BOLD}random{Color.RESET}.",
        2: f"The {Color.MAGENTA}{Color.BOLD}Sanctuaries{Color.RESET} were already hollow when they struck.",
        3: f"The first {Color.RED}{Color.BOLD}demons{Color.RESET} emerged years after the stars fell.",
        4: f"Something was {Color.YELLOW}{Color.BOLD}sealed{Color.RESET} before it was broken.",
        5: f"{Color.MAGENTA}{Color.BOLD}Lilith{Color.RESET} did not descend from the heavens.",
        6: f"The {Color.MAGENTA}{Color.BOLD}Sanctuaries{Color.RESET} were constructed, not formed.",
        7: f"Ancient {Color.CYAN}{Color.BOLD}runes{Color.RESET} predate mortal civilization.",
        8: f"The night sky once held a {Color.YELLOW}{Color.BOLD}star{Color.RESET} that is gone.",
        9: f"{Color.RED}{Color.BOLD}Demons{Color.RESET} do not fear death — they fear silence.",
        10: f"Fragments resonate with something still {Color.CYAN}{Color.BOLD}sleeping{Color.RESET}.",
        11: f"Corrupted {Color.GREEN}{Color.BOLD}Hunters{Color.RESET} hear whispers before change.",
        12: f"{Color.MAGENTA}{Color.BOLD}Lilith{Color.RESET} was the first to awaken — not to exist.",
        13: f"The {Color.MAGENTA}{Color.BOLD}Sanctuaries{Color.RESET} are {Color.RED}{Color.BOLD}prisons{Color.RESET}.",
        14: f"{Color.MAGENTA}{Color.BOLD}Lilith{Color.RESET} was born inside the deepest {Color.MAGENTA}{Color.BOLD}Sanctuary{Color.RESET}.",
        15: f"The {Color.RED}{Color.BOLD}demons{Color.RESET} are fragments of a greater whole.",
        16: f"{Color.GREEN}{Color.BOLD}Hunters{Color.RESET} absorb more than power — they absorb memory.",
        17: f"The falling {Color.YELLOW}{Color.BOLD}stars{Color.RESET} were pieces of a shattered being.",
        18: f"That being was broken by the {Color.CYAN}{Color.BOLD}gods{Color.RESET}.",
        19: f"Not all {Color.YELLOW}{Color.BOLD}fragments{Color.RESET} fell to the earth.",
        20: f"The final {Color.YELLOW}{Color.BOLD}fragment{Color.RESET} never left the sky.",
        21: f"{Color.MAGENTA}{Color.BOLD}Lilith{Color.RESET} seeks not conquest — but reunion.",
        22: f"When all {Color.YELLOW}{Color.BOLD}fragments{Color.RESET} unite, the {Color.RED}{Color.BOLD}Prisoner{Color.RESET} awakens."
    }
    # Display lore fragment for the completed quest
    if quest_id in lore_fragments:
        print(f"\n{Color.MAGENTA}{Color.BOLD}Lore Fragment Uncovered:{Color.RESET}")
        print(f"\"{lore_fragments[quest_id]}\"")
        pause()

    # Leveling
    new_xp, new_level, max_health, leveled_up = process_leveling(current_xp, current_level, exp_gained)
    if leveled_up:
        current_health = min(current_health, max_health)

    # Mark quest as complete

    # Check if this quest is already in quest_progress for this save
    cursor.execute("""
        SELECT id FROM quest_progress 
        WHERE save_id = %s AND quest_id = %s
    """, (save_id, quest_id))
    existing = cursor.fetchone()

    if existing:
        # Update existing record
        cursor.execute("""
            UPDATE quest_progress
            SET completed = 1, completed_at = %s
            WHERE id = %s
        """, (datetime.now(), existing[0]))
    else:
        # Insert new record
        cursor.execute("""
            INSERT INTO quest_progress (save_id, quest_id, completed, completed_at)
            VALUES (%s, %s, 1, %s)
        """, (save_id, quest_id, datetime.now()))

    # Update player stats
    cursor.execute("""
        UPDATE player_stats 
        SET xp = %s, level = %s, max_health = %s, health = %s
        WHERE save_id = %s
    """, (new_xp, new_level, max_health, current_health, save_id,))

    conn.commit()
    cursor.close()

    completion_rows = [
        ["XP Gained", c(exp_gained, Color.YELLOW)],
        ["New XP", c(new_xp, Color.CYAN)],
        ["Level", c(new_level, Color.GREEN)],
        ["Health", c(current_health, Color.RED)]
    ]

    table("Quest Completed!", ["Result", "Value"], completion_rows)
    time.sleep(random.uniform(0.4, 0.6)) 
    pause()

    if leveled_up:
        level_rows = [
            ["New Level", c(new_level, Color.GREEN)],
            ["New Max Health", c(max_health, Color.RED)]
        ]
        table("🔥 LEVEL UP! 🔥", ["Upgrade", "Value"], level_rows)
        pause()

    # Reward Section
    quest_reward(conn, save_id, quest_id)

    return True