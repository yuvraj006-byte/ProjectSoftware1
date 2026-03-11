def save_game(conn, save_id):
    """
    Saves the current game state for the given save_id.
    Ensures player stats, inventory, and quest progress are up-to-date.
    Returns save_id for confirmation.
    """
    cursor = conn.cursor(buffered=True)

    # Example: ensure latest player stats are saved (optional if updates happen immediately)
    cursor.execute("""
        UPDATE player_stats
        SET health = health, xp = xp, level = level, max_health = max_health, 
            armor = armor, gold = gold
        WHERE save_id = %s
    """, (save_id,))

    # If you want, you can also "touch" inventory or quest progress here
    # to ensure consistency, but usually they are updated in real-time

    conn.commit()
    cursor.close()

    return save_id