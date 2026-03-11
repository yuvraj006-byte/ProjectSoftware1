def combat_log(conn, save_id, enemy_id, xp_gained):
    cursor = conn.cursor(buffered=True)
    sql = """
        INSERT INTO combat_log (enemy_id, save_id, xp_earned)
        VALUES (%s, %s, %s);
        """
    cursor.execute(sql, (enemy_id, save_id, xp_gained))
    conn.commit()
    cursor.close()