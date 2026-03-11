def get_equipped_armor(conn, save_id):
    cursor = conn.cursor(buffered=True)

    cursor.execute("""
        SELECT items.defense_bonus
        FROM inventory
        JOIN items ON inventory.item_id = items.id
        WHERE inventory.save_id = %s
        AND inventory.equipped = TRUE
        AND items.item_type = 'armor'
        LIMIT 1
    """, (save_id,))

    result = cursor.fetchone()
    cursor.close()

    if result:
        return int(result[0] or 0) * 2  # your armor multiplier

    return 0