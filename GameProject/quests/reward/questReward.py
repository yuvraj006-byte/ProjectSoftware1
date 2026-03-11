class Color:
    YELLOW = "\033[1;33m"
    RESET = "\033[0m"
    BOLD = "\033[1;31m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

def quest_reward(conn, save_id, quest_id):
    cursor = conn.cursor()
    
    cursor.execute("SELECT reward_gold FROM quests WHERE id = %s;", (quest_id,))
    result = cursor.fetchone()
    
    if not result:
        return False  # Quest not found
    
    quest_gold = result[0]
    
    cursor.execute(
        "UPDATE player_stats SET gold = gold + %s WHERE save_id = %s;",
        (quest_gold, save_id)
    )
    
    print(f"You Earned {Color.YELLOW}{Color.BOLD}{quest_gold}{Color.RESET} Gold!")

    conn.commit()
    return True