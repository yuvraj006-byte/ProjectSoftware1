import json
import random

def get_enemy(conn, region):
    cursor = conn.cursor(buffered=True)

    # Base SQL query: get all enemies for the region except Lilith
    sql = """
        SELECT id,
               name,
               type,
               base_health,
               base_attack, 
               base_defence,
               total_health,
               xp_drop,
               attacks
        FROM enemies
        WHERE region = %s 
        AND name != 'Lilith';
    """
    cursor.execute(sql, (region,))
    enemies = cursor.fetchall()
    cursor.close()

    if not enemies:
        return None

    # Special handling for region "black"
    if region.lower() == "black":
        # Increase Lucifer's probability
        weighted_enemies = []
        for enemy in enemies:
            name = enemy[1]
            if name.lower() == "lucifer":
                # Give Lucifer extra weight, e.g., 5 times more likely
                weighted_enemies.extend([enemy] * 5)
            else:
                weighted_enemies.append(enemy)
        selected_enemy = random.choice(weighted_enemies)
    else:
        # Randomly select 1 enemy for other regions
        selected_enemy = random.choice(enemies)

    # Convert JSON string → Python dictionary
    attacks_dict = json.loads(selected_enemy[8])
    attacks_list = list(attacks_dict.values())

    return {
        "id": selected_enemy[0],
        "name": selected_enemy[1],
        "type": selected_enemy[2],
        "base_health": selected_enemy[3],
        "base_attack": selected_enemy[4],
        "base_defence": selected_enemy[5],
        "total_health": selected_enemy[6],
        "xp_drop": selected_enemy[7],
        "attack_type": attacks_list
    }