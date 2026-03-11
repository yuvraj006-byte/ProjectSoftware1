def load_game(conn, save_id):
    cursor = conn.cursor(dictionary=True, buffered=True)

    # Player Stats
    cursor.execute("""
        SELECT location, level, xp, health, max_health, armor, gold, demons_defeated
        FROM player_stats
        WHERE save_id = %s
    """, (save_id,))
    stats = cursor.fetchone()

    if not stats:
        cursor.close()
        raise ValueError(f"No player stats found for save_id {save_id}")

    # Inventory
    cursor.execute("""
        SELECT inventory.item_id, item_name, inventory.quantity, inventory.equipped, items.item_type, items.value_in_gold
        FROM inventory
        JOIN items ON inventory.item_id = items.id
        WHERE inventory.save_id = %s
    """, (save_id,))
    inventory = cursor.fetchall()

    # Quest Progress
    cursor.execute("""
        SELECT quests.id, quests.quest_name, quest_progress.completed
        FROM quest_progress
        JOIN quests ON quest_progress.quest_id = quests.id
        WHERE quest_progress.save_id = %s
    """, (save_id,))
    quests = cursor.fetchall()

    cursor.close()
    return stats, inventory, quests