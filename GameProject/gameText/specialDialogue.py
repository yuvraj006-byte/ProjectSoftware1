from gameText.npcDialogues import total_dialogues

def dialogue_if_no_kill():
    return [
        "First hunt?\nKill one. Just one. Then come back."
    ]


def dialogue_if_low_health():
    return [
        "You look like death already claimed half of you.\nRest before you fly again."
    ]


def dialogue_if_more_than_20_kills():
    return [
        "You're starting to carry their scent.\nThe stronger you get… the more they'll notice."
    ]


def special_dialogue(conn, save_id):
    cursor = conn.cursor(dictionary=True)

    query = """ 
    SELECT demons_defeated,
           health,
           max_health
    FROM player_stats
    WHERE save_id = %s;
    """

    cursor.execute(query, (save_id,))
    result = cursor.fetchone()
    cursor.close()

    demon_count = result["demons_defeated"]
    player_health = result["health"]
    player_max_health = result["max_health"]

    if demon_count == 0:
        if player_health < (0.3 * player_max_health):
            print(dialogue_if_low_health()[0])
        else:
            print(dialogue_if_no_kill()[0])

    elif demon_count >= 20:
        print(dialogue_if_more_than_20_kills()[0])

    elif player_health < (0.3 * player_max_health):
        print(dialogue_if_low_health()[0])
    else:
        total_dialogues()