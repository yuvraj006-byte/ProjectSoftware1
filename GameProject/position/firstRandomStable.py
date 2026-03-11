import random
import time
from .firstRandomCity import get_first_random_city

def get_first_random_stable(conn):

    def get_stable(city_id):
        cursor = conn.cursor(buffered=True)

        sql = """
        SELECT id, stable_name
        FROM stables
        WHERE city_id = %s
        """

        cursor.execute(sql, (city_id,))
        results = cursor.fetchall()

        if not results:
            cursor.close()
            raise ValueError(f"No stables found for city: {city_id}")

        result = random.choice(results)
        cursor.close()

        return result[0], result[1]   # return both ID and name

    cityId, cityName, region = get_first_random_city(conn)
    stableId, name = get_stable(cityId)

    # Lines to display
    lines = [
        f"Your first stable is waiting for you in \033[1;36m{cityName}\033[0m, and its name is \033[1;33m{name}\033[0m!",
        "\033[1;32mThis is just the beginning of your journey!\033[0m",
        "As you explore the world of \033[1;36mOpen Skies\033[0m, you'll discover more stables, each giving you new ways to travel and uncover hidden secrets.",
        "Master the skies, reach distant lands, and prepare yourself for the ultimate challenges that lie ahead!"
    ]

    # Print with a short delay for readability
    for line in lines:
        print(line)
        time.sleep(random.uniform(0.4, 0.7))  # quick, not boring

    return stableId, region