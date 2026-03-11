LEVEL_XP_THRESHOLD = 100
BASE_HEALTH = 236
HEALTH_GROWTH_RATE = 1.1
MAX_HEALTH_CAP = 30000  # new cap


def calculate_max_health(level: int) -> int:
    return int(BASE_HEALTH * (HEALTH_GROWTH_RATE ** (level - 1)))


def process_leveling(current_xp: int, current_level: int, xp_gained: int):
    new_xp_total = current_xp + xp_gained
    new_level = current_level
    leveled_up = False

    # Level-up loop
    while new_xp_total >= LEVEL_XP_THRESHOLD:
        new_xp_total -= LEVEL_XP_THRESHOLD
        new_level += 1
        leveled_up = True

    # Calculate max health and cap it at MAX_HEALTH_CAP
    max_health = calculate_max_health(new_level)
    max_health = min(max_health, MAX_HEALTH_CAP)

    return new_xp_total, new_level, max_health, leveled_up