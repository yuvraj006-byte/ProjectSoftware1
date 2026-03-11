import time
import random
from tabulate import tabulate
from items.store import store
from position.travel import travel
from gameText.preFinal import pre_final
from getStats.getStats import get_stats
from combat.combatLog import combat_log
from gameState.saveGame import save_game
from quests.questWrap import full_quest_wrap
from inventory.inventory import get_inventory
from combat.items.equipItem import equip_item
from combat.combat import compiled_combat_func       
from playerUI.levelingUp import process_leveling
from gameText.bossDefeated import boss_defeated
from gameText.specialDialogue import special_dialogue       
from gameText.environments import environments_output    
from combat.items.demonicDrop import demonic_spirit_drop
from position.availableStables import get_available_stables  
from butlerUI.butlerUI import butler_4, butler_10, butler_11, butler_13, butler_14, butler_15, butler_16, butler_17, butler_18
class Color:
    CYAN           = "\033[1;36m"
    YELLOW         = "\033[1;33m"
    GREEN          = "\033[1;32m"
    MAGENTA        = "\033[1;35m"
    BRIGHT_BLACK   = "\033[1;30m"
    RED            = "\033[1;31m"
    RESET          = "\033[0m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"


def table(title, headers, rows, tablefmt="fancy_grid"):
    print(f"\n{c(title, Color.MAGENTA)}")
    print(tabulate(rows, headers=headers, tablefmt=tablefmt))

def pause():
    input('\033[32mPress Enter to continue...\033[0m') 

# ---------------------- MENU ----------------------
def game_menu():
    menu_data = [
        ["Butler", "Summon Butler"],
        ["1", "Explore The World"],
        ["2", "Check Your Inventory"],
        ["3", "View Your Stats"],
        ["4", "See Quests"],
        ["5", "Talk To Stable Master"],
        ["6", "Equip Items"],
        ["7", "Kill Demons"],
        ["8", "Heal"],
        ["9", "Open Store"],
        ["0", "Save/Exit Game"]
    ]

    colored_menu = [[c(row[0], Color.CYAN), row[1]] for row in menu_data]

    table("What Would You Like To Do?", ["Option", "Action"], colored_menu)

    return input("Enter choice: ").strip().lower()
# ---------------------- PLAYER LOCATION ----------------------
def get_player_location(conn, save_id):
    """Return current city ID and region directly from DB."""
    cursor = conn.cursor(buffered=True)
    cursor.execute("""
        SELECT cities.id, nations.region
        FROM player_stats
        INNER JOIN stables ON player_stats.location = stables.id
        INNER JOIN cities ON stables.city_id = cities.id
        INNER JOIN nations ON cities.nation_id = nations.id
        WHERE player_stats.save_id = %s
    """, (save_id,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        city_id, region = result
        return city_id, region
    return None, None

# ---------------------- MENU ACTIONS ----------------------
def menu_result(conn, save_id, choice, player_health):
    """Process menu selection. Returns updated health."""
    
    city_id, region = get_player_location(conn, save_id)  # always fresh    

    if choice == "1":  # Explore
        pause()
        stables = get_available_stables(conn, save_id)

        print("\nAvailable Stables:")
        rows = []

        for stable in stables:
            rows.append([
                c(stable["id"], Color.GREEN),
                c(stable["stable_name"], Color.YELLOW),
                c(stable["city_name"], Color.MAGENTA),
                c(stable["region"], Color.CYAN)
            ])

        table("Available Stables", ["ID", "Stable", "City", "Region"], rows)

        # create list of allowed IDs
        valid_ids = [stable["id"] for stable in stables]

        travel(conn, save_id, valid_ids)
        if region == 'Black':
            pre_final()
        pause()

    elif choice == "2":
        pause()
        inventory = get_inventory(conn, save_id)

        if not inventory:
            print(c("Your inventory is empty.", Color.RED))
            pause()
            return player_health

        rows = []
        for item in inventory:
            rows.append([
                c(item["item_name"], Color.GREEN),
                c(item["item_type"], Color.YELLOW),
                c(item["quantity"], Color.CYAN),
                c(item["equipped"], Color.MAGENTA),
                c(item["value_in_gold"], Color.YELLOW)
            ])

        table("Your Inventory",
            ["Item", "Type", "Qty", "Equipped", "Value"],
            rows)

        pause()

    elif choice == "3":
        pause()
        stats = get_stats(conn, save_id)

        if not stats:
            print("No stats available.")
            pause()
            return player_health

        labels = [
            "Save ID","Location", "Level", "XP", "Health",
            "Max Health", "Armor", "Gold",
            "Demons Defeated"
        ]

        rows = []
        for label, value in zip(labels, stats):
            rows.append([label, c(value, Color.BRIGHT_BLACK)])

        table("Your Stats", ["Attribute", "Value"], rows)
        pause()

    elif choice == "4":  # Quests
        pause()
        print("\nAvailable Quests:")
        full_quest_wrap(conn, save_id, region)  # fetches region internally
        pause()

    elif choice == "5":  # Stable Master
        pause()
        special_dialogue(conn, save_id)
        pause()

    elif choice == "6":  # Equip Items
        pause()
        equip_item(conn, save_id)

    elif choice == "7":  # Combat
        pause()
        environments_output()
        pause()

        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT health, xp, level, max_health FROM player_stats WHERE save_id = %s", (save_id,))
        result = cursor.fetchone()
        cursor.close()

        if not result:
            print("Error loading player stats.")
            return player_health

        player_health, current_xp, current_level, max_health = result

        if player_health <= 0:
            butler_4()
            pause()
            return player_health

        xp, player_health, kills, enemy_id = compiled_combat_func(conn, save_id, region, player_health)
        new_xp, new_level, new_max_health, leveled_up = process_leveling(current_xp, current_level, xp)
        if leveled_up:
            player_health = new_max_health

        cursor = conn.cursor(buffered=True)
        cursor.execute("""
            UPDATE player_stats
            SET xp = %s, level = %s, max_health = %s, health = %s, demons_defeated = demons_defeated + %s
            WHERE save_id = %s
        """, (new_xp, new_level, new_max_health, player_health, kills, save_id))
        conn.commit()
        cursor.close()

        combat_log(conn, save_id, enemy_id, xp)

        # Only roll drop if something was actually killed
        if kills > 0:
            item_data, item_id = demonic_spirit_drop(conn, region)
        else:
            item_data, item_id = None, None
        if item_data:
            # Dramatic drop message
            print(c("\n☠ You strike the final blow.", Color.RED))
            time.sleep(random.uniform(0.3, 0.5))
            print(c("The Demon lets out a shattered scream as its body collapses into ash...", Color.RED))
            time.sleep(random.uniform(0.3, 0.5))
            print(c("From the fading embers, its Demonic Spirit remains.\n", Color.MAGENTA))
            time.sleep(random.uniform(0.4, 0.6))

            reward_rows = [
                ["Item", c(item_data["Name"], Color.GREEN)],
                ["Skills", c(item_data["Skills"], Color.CYAN)]
            ]

            table("🔥 Demonic Drop", ["Reward Type", "Details"], reward_rows)
            time.sleep(random.uniform(0.4, 0.6)) 
            
            cursor = conn.cursor(buffered=True)
            cursor.execute(
                "SELECT quantity FROM inventory WHERE save_id = %s AND item_id = %s",
                (save_id, item_id)
            )
            existing = cursor.fetchone()

            if existing:
                cursor.execute(
                    "UPDATE inventory SET quantity = quantity + 1 WHERE save_id = %s AND item_id = %s",
                    (save_id, item_id)
                )
            else:
                cursor.execute(
                    "INSERT INTO inventory (save_id, item_id, quantity, equipped) VALUES (%s, %s, 1, 0)",
                    (save_id, item_id)
                )

            conn.commit()
            cursor.close()

        summary_rows = [
            ["XP Gained", c(xp, Color.YELLOW)],
            ["Demons Defeated", c(kills, Color.GREEN)],
            ["Remaining Health", c(player_health, Color.RED)]
        ]

        table("Combat Summary", ["Result", "Value"], summary_rows)
        time.sleep(random.uniform(0.4, 0.6)) 

        if enemy_id == 8:
            boss_defeated()
            exit()
    
        pause()

    elif choice == "8":  # Heal
        cursor = conn.cursor(buffered=True)
        cursor.execute("UPDATE player_stats SET health = max_health WHERE save_id = %s;", (save_id,))
        conn.commit()
        cursor.execute("SELECT max_health FROM player_stats WHERE save_id = %s", (save_id,))
        result = cursor.fetchone()
        player_health = result[0] if result else player_health
        cursor.close()

        healing_effects = [
            "A surge of vitality courses through you, mending flesh and spirit alike.",
            "Golden light wraps around you, knitting your wounds with precision.",
            "You inhale sharply, and with it comes strength—a resurgence of your essence."
        ]
        print(random.choice(healing_effects))
        pause()

    elif choice == "9":  # Store
        store(conn, save_id)
        pause()

    elif choice == "0":  # Exit
        while True:
            exit_choice = input("Do You Want to Save The Game? (Y/N): ").strip().lower()
            if exit_choice == 'y':
                save_game(conn, save_id)
                butler_10(save_id)
                exit()
            elif exit_choice == 'n':
                butler_11()
                pause()
                print()
                confirm = input("Do You Chose To Not Save? (Y/N): ").strip().lower()
                if confirm == 'y':                    
                    exit()
                else:
                    continue
            else:
                print("Invalid Choice! Try Again!")
    
    elif choice == "butler":
        butler_13()
        pause()
        print()

        butler_menu_data = [
            ["1", "Why Are You Here?"],
            ["2", "Who You Are?"],
            ["3", "Role Of Butler."],
            ["4", "Who Is Ther Butler?"]
        ]

        colored_butler_menu = [[c(row[0], Color.CYAN), row[1]] for row in butler_menu_data]
        table("What Would You Like To Do?", ["Option", "Action"], colored_butler_menu)
        butler_choice = input("Enter choice: ").strip().lower()

        if butler_choice == "1":
            butler_14()
        elif butler_choice == "2":
            butler_15()
        elif butler_choice == "3":
            butler_17()
        elif butler_choice == "4":
            butler_16()
        else: 
            butler_18()

    else:
        pause()
        print("Invalid choice. Please select a valid option.")
        pause()

    return player_health
