def create_new_save(conn, user_id, save_name, starting_location):
    cursor = conn.cursor(buffered=True)

    # 1️⃣ Create the save
    cursor.execute(
        "INSERT INTO game_saves (user_id, save_name) VALUES (%s, %s)",
        (user_id, save_name)
    )
    conn.commit()
    save_id = cursor.lastrowid  # get the new save's ID

    # 2️⃣ Create the starting stats for this save
    starting_stats = {
        "level": 1,
        "xp": 0,
        "health": 236,
        "max_health": 236,
        "armor": 0,
        "gold": 50,
        "demons_defeated": 0,
    }

    cursor.execute("""
        INSERT INTO player_stats (
            save_id, location, level, xp, health, max_health, armor, gold, demons_defeated
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        save_id,
        starting_location,
        starting_stats["level"],
        starting_stats["xp"],
        starting_stats["health"],
        starting_stats["max_health"],
        starting_stats["armor"],
        starting_stats["gold"],
        starting_stats["demons_defeated"]
    ))

    conn.commit()
    cursor.close()

    return save_id