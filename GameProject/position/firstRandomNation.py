class Color:
    CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    GREEN = "\033[1;32m"
    MAGENTA = "\033[1;35m"
    RED = "\033[1;31m"
    RESET = "\033[0m"
    BLACK = "\033[1;30m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

def starting_position(conn):
    def get_nation(what_empire):
        cursor = conn.cursor()
        sql = """
        SELECT nation_name, region
        FROM nations
        WHERE empire = %s
        ORDER BY RAND()
        LIMIT 1
        """
        cursor.execute(sql, (what_empire,))
        result = cursor.fetchone()
        cursor.close()
        return result  

    empire_dic = {
        "MU": "Mustafar",
        "NE": "Nepotis",
        "KA": "Kamino",
        "AR": "Arkania",
        "GE": "Geonosis"
    }
    
    print()
    for key, value in empire_dic.items():
        print(f"{key}: {value}")
   
    while True:
        empire = input("Choose Your Starting Empire!: ").strip().upper()
        if empire in empire_dic:
            empire_name = empire_dic[empire]
            result = get_nation(empire_name)
            if result is None:
                print(c(f"No nations found for {empire_name}!", Color.RED))
                continue

            nation, region = result
            print(f"\nYour Starting Nation Is: {c(nation, Color.GREEN)} In The Empire Of {c(empire_name, Color.CYAN)}!")
            print(f"It Is a {region} Region!")
            return nation, region
        else:
            print(c("This Empire Does Not Exist In The World of Open Skies", Color.RED))