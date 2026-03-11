
# Function that gets the player's current stable and city from the database
def get_player_location(conn, save_id):

    # Create a database cursor that returns results as dictionaries
    cursor = conn.cursor(dictionary=True, buffered=True)

    # SQL query to find the player's current stable and the city it belongs to
    query = """
        SELECT
            stables.id,
            stables.stable_name,
            cities.id AS city_id,
            cities.city_name
        FROM player_stats
        JOIN stables ON player_stats.location = stables.id
        JOIN cities ON stables.city_id = cities.id
        WHERE player_stats.save_id = %s
        LIMIT 1
    """

    # Execute the query using the player's save_id
    cursor.execute(query, (save_id,))

    # Fetch the first result (the player's location)
    result = cursor.fetchone()

    # Close the cursor
    cursor.close()

    # Return the player's location data
    return result



# Function that finds which stables the player can travel to
# It calculates the shortest distance between cities using Dijkstra's algorithm
def get_available_stables(conn, save_id, max_distance=1000):

    # ----------------------------
    # STEP 1: Get player location
    # ----------------------------

    # Get the player's current stable and city
    location = get_player_location(conn, save_id)

    # If the player has no location, return an empty list
    if not location:
        return []

    # Store the player's starting city
    start_city = location["city_id"]


    # ----------------------------
    # STEP 2: Load city graph
    # ----------------------------

    # Create a database cursor
    cursor = conn.cursor(dictionary=True, buffered=True)

    # Get all city connections and their distances
    cursor.execute("SELECT city1_id, city2_id, distance FROM city_connections")

    # Fetch all results
    rows = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Create an empty graph dictionary
    # This will store cities and their connected neighbors
    graph = {}

    # Loop through all city connections
    for row in rows:

        # Get both connected cities
        c1 = row["city1_id"]
        c2 = row["city2_id"]

        # Get the distance between them
        dist = float(row["distance"])

        # If city1 is not in the graph yet, add it
        if c1 not in graph:
            graph[c1] = []

        # If city2 is not in the graph yet, add it
        if c2 not in graph:
            graph[c2] = []

        # Add connection from city1 to city2
        graph[c1].append((c2, dist))

        # Add connection from city2 to city1 (since travel works both ways)
        graph[c2].append((c1, dist))


    # ----------------------------
    # STEP 3: Simple Dijkstra Algorithm
    # ----------------------------

    # Dictionary that will store the shortest known distance to each city
    distances = {}

    # List of cities that have already been processed
    visited = []

    # Initialize distances for all cities as infinity
    # This means we don't yet know how far they are
    for city in graph:
        distances[city] = float("inf")

    # The starting city distance is 0 because we are already there
    distances[start_city] = 0


    # Continue searching until we break the loop
    while True:

        # These variables will track the closest unvisited city
        current_city = None
        current_min_distance = float("inf")

        # Find the closest city that hasn't been visited yet
        for city in distances:
            if city not in visited and distances[city] < current_min_distance:
                current_city = city
                current_min_distance = distances[city]

        # Stop if no city can be found
        if current_city is None:
            break

        # Stop if the closest city is farther than the allowed travel distance
        if current_min_distance > max_distance:
            break

        # Mark this city as visited
        visited.append(current_city)

        # Check all neighboring cities connected to this city
        for neighbor, weight in graph.get(current_city, []):

            # Calculate distance to the neighbor through this city
            new_distance = distances[current_city] + weight

            # If the new path is shorter, update the stored distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance


    # ----------------------------
    # STEP 4: Collect reachable cities
    # ----------------------------

    # List that will contain cities reachable within the distance limit
    reachable_cities = []

    # Loop through all calculated distances
    for city, dist in distances.items():

        # Add cities that are within the allowed travel distance
        # We exclude the starting city (distance 0)
        if 0 < dist <= max_distance:
            reachable_cities.append(city)

    # If no cities are reachable, return an empty list
    if not reachable_cities:
        return []


    # ----------------------------
    # STEP 5: Fetch stables
    # ----------------------------

    # Create a new database cursor
    cursor = conn.cursor(dictionary=True, buffered=True)

    # Create placeholders (%s) for the SQL IN query
    format_strings = ",".join(["%s"] * len(reachable_cities))

    # Query to fetch stables located in reachable cities
    query = f"""
            SELECT 
                stables.id,
                stables.stable_name,
                stables.city_id,
                cities.city_name,
                nations.region
            FROM stables
            JOIN cities ON stables.city_id = cities.id
            JOIN nations ON cities.nation_id = nations.id
            WHERE stables.city_id IN ({format_strings})
        """

    # Execute the query with the reachable city IDs
    cursor.execute(query, tuple(reachable_cities))

    # Fetch all matching stables
    stables = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Return the list of reachable stables
    return stables