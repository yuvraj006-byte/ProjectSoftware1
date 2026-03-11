def demonic_spirit_drop(conn, current_region):
    cursor = conn.cursor(dictionary=True, buffered=True)

    query = """
        SELECT id, item_name, skill_1, skill_2, skill_3, skill_4
        FROM items
        WHERE region = %s
        AND item_type != 'Shields' 
        ORDER BY RAND()
        LIMIT 1
    """

    cursor.execute(query, (current_region,))
    item = cursor.fetchone()
    cursor.close()

    if not item:
        return None, None

    # Collect skills into list
    skills = [
        item['skill_1'],
        item['skill_2'],
        item['skill_3'],
        item['skill_4']
    ]
    skills = list(filter(None, skills))

    # ANSI bold formatting
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Return skills as a single string with proper formatting
    if not skills:
        skills_str = ""
    elif len(skills) == 1:
        skills_str = skills[0]
    else:
        skills_str = ", ".join(skills)

    items = {
        "Name": f"{BOLD}{item['item_name']}{RESET}",
        "Skills": f"{BOLD}{skills_str}{RESET}"
    }

    return items, item["id"]