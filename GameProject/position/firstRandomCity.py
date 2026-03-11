import random
from .firstRandomNation import starting_position

def get_first_random_city(conn):    
    def get_city(what_nation):
        cursor = conn.cursor(buffered=True)

        sql = """
        SELECT cities.id, cities.city_name
        FROM cities
        JOIN nations ON cities.nation_id = nations.id
        WHERE nations.nation_name = %s
        """

        cursor.execute(sql, (what_nation,))
        results = cursor.fetchall()
        
        if not results:
            cursor.close()
            raise ValueError(f"No cities found for nation: {what_nation}")
        
        result = random.choice(results)

        cursor.close()

        return result
    nation, region = starting_position(conn)
    cityId, cityName = get_city(nation)

    return cityId, cityName, region