from combat.items.armor import get_equipped_armor

def recalculate_player_stats(conn, save_id):
    armor = get_equipped_armor(conn, save_id)

    cursor = conn.cursor()
    cursor.execute("""
        UPDATE player_stats
        SET armor = %s
        WHERE save_id = %s
    """, (armor, save_id))
    conn.commit()
    cursor.close()


def get_stats(conn, save_id):
    recalculate_player_stats(conn, save_id)
    cursor = conn.cursor(buffered=True)
    sql = """
    SELECT *
    FROM player_stats
    WHERE save_id = %s
    """
    cursor.execute(sql, (save_id,))
    stats = cursor.fetchone()
    cursor.close()
    return stats