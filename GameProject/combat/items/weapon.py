def get_equipped_weapon(conn, save_id):
    cursor = conn.cursor(buffered=True)

    cursor.execute("""
        SELECT items.attack_bonus
        FROM items
        JOIN inventory ON items.id = inventory.item_id
        WHERE inventory.save_id = %s
          AND inventory.equipped = TRUE
          AND items.item_type = 'weapons'
        LIMIT 1
    """, (save_id,))

    result = cursor.fetchone()
    cursor.close()

    if result:
        return int(result[0] or 1)

    return 5  # default attack if no weapon equipped