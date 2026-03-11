from gameText.worldHistory import world_history
from items.firstItems import get_random_loadout
from position.firstRandomStable import get_first_random_stable


def pause():
    input('\033[32mPress Enter to continue...\033[0m') 

def player_ui(conn, user_id):
    """Initialize player UI: first stable, first item, and player health."""

    # Get player health
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT health FROM player_stats WHERE user_id = %s;", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    player_health = result[0] if result else 0

    pause()

    # Get first stable and assign to player
    first_stable_id, region = get_first_random_stable(conn)

    pause()
    print("\nYou will now receive your first set of items!")
    item, item_id = get_random_loadout(conn, region)

    print("\nYour first item:")
    for key, value in item.items():
        print(f"{key.capitalize()}: {value}")
    pause()

    return first_stable_id, item_id, player_health