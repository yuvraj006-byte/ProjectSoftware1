import random
from butlerUI.butlerUI import butler_4
from combat.enemies.enemies import get_enemy
from combat.bossFight.finalBoss import final_boss
from combat.items.armor import get_equipped_armor
from combat.items.weapon import get_equipped_weapon

def pause():
    input('\033[32mPress Enter to continue...\033[0m') 

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

def compiled_combat_func(conn, save_id, region, player_health):

    # Get enemy for current region
    enemy = get_enemy(conn, region)

    # Get player's equipped item attack and armor
  
    player_base_attack = get_equipped_weapon(conn, save_id)

    armor = get_equipped_armor(conn, save_id)

    if enemy is None:
        print("No enemies available in this region. Try another region!")
        return 0, player_health, 0  # no XP, no demons defeated

    # Enemy stats
    enemy_name = enemy.get("name", "Unknown Demon")
    enemy_health = int(enemy.get("total_health", 10))
    enemy_base_attack = int(enemy.get("base_attack", 1))
    xp_drop = int(enemy.get("xp_drop", 0))
    enemy_attack_type = enemy.get("attack_type")
    enemy_id = enemy.get("id")

    if enemy_name == "Lucifer": 
        final_boss()
        print()
        pause()
    xp_gained = 0
    demons_defeated = 0

    print(c("\n🔥 You Encountered A Demon! 🔥", Color.MAGENTA))
    print(f"{c('Name', Color.CYAN)}: {enemy_name}")
    print(f"{c('Enemy Health', Color.CYAN)}: {enemy_health}")
    print(f"{c('Enemy Attack', Color.CYAN)}: {enemy_base_attack}")
    print(f"{c('Your Health', Color.CYAN)}: {player_health}\n")

    # --------- Combat Loop ----------
    while enemy_health > 0 and player_health > 0:

        # Ask player to attack
        while True:
            attack_choice = input("Do You Wish To Attack? (Y/N): ").strip().lower()
            if attack_choice in ("y", "n"):
                break
            print("Invalid choice. Please enter Y or N.")

        if attack_choice == "n":
            print(c("You fled from battle!", Color.YELLOW))
            return 0, player_health, 0, enemy_id

        # ---- Player Attacks ----
        player_attack = random.randint(
            max(1, int(player_base_attack * 1.2)),
            max(1, int(player_base_attack * 2))
        )

        enemy_health -= player_attack
        enemy_health = max(enemy_health, 0)

        print(c("⚔ You dealt", Color.GREEN), f"{player_attack} damage!")
        print(f"{enemy_name}'s remaining health: {enemy_health}\n")

        if enemy_health <= 0:
            xp_gained = xp_drop
            demons_defeated = 1
            print(c("💀 You killed the demon!", Color.MAGENTA))
            print(f"You gained {xp_gained} XP!\n")
            break

        # ---- Enemy Attacks ----
        demon_attack = random.randint(
            max(1, int(enemy_base_attack * 0.8)),
            max(1, int(enemy_base_attack * 1.2))
        )

        damage_multiplier = 100 / (100 + armor) 
        reduced_damage = max(1, int(demon_attack * damage_multiplier))
        player_health -= reduced_damage
        player_health = max(player_health, 0)

        print()
        print(c(f"{random.choice(enemy_attack_type)}!", Color.YELLOW), "BE CAREFUL!!")
        print(c("☠ The demon attacked for", Color.RED), f"{demon_attack} damage! (Reduced to {reduced_damage} by armor)")
        print(f"Your remaining health: {player_health}\n")

        if player_health <= 0:
            print(c("💀 You died!", Color.RED))
            butler_4()
            break
    
    return xp_gained, player_health, demons_defeated, enemy_id

# THIS IS TO DEBUG SO THAT THERE IS SOMETHING TO FALL BASCK TO IF SOMEHOW THESE FUNCITONS DO NOT WORK


def items():
    return None


def items():
    return None


def bossFight():
    return None


def enemies():
    return None