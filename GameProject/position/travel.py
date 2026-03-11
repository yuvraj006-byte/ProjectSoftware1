from butlerUI.butlerUI import butler_3


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


def travel_cost(conn, save_id):
    cursor = conn.cursor(buffered=True)

    cursor.execute(
        "SELECT gold FROM player_stats WHERE save_id = %s;",
        (save_id,)
    )

    result = cursor.fetchone()
    cursor.close()

    player_gold = int(result[0])

    # show gold vs travel cost
    butler_3(player_gold, 40)

    if player_gold >= 40:
        return True
    else:
        return False


def travel(conn, save_id, valid_ids):

    while True:

        is_travel = input("Do you want to travel to a new stable? (Y/N): ").strip().lower()

        if is_travel == "y":

            if not travel_cost(conn, save_id):
                print(c("You don't have enough gold to travel.", Color.RED))
                return

            while True:

                travel_id_input = input("Enter the ID of the stable you want to travel to: ").strip()

                try:
                    travel_id = int(travel_id_input)
                except ValueError:
                    print(c("Please enter a valid number.", Color.RED))
                    continue

                if travel_id not in valid_ids:
                    print(c("Please choose an ID from the available stables.", Color.RED))
                    continue

                cursor = conn.cursor(buffered=True)

                query = """
                        SELECT stables.id, stables.stable_name, nations.region, cities.city_name
                        FROM stables
                        INNER JOIN cities ON stables.city_id = cities.id
                        INNER JOIN nations ON cities.nation_id = nations.id
                        WHERE stables.id = %s
                        """

                cursor.execute(query, (travel_id,))
                stable = cursor.fetchone()

                if stable:

                    print(
                        f"Traveling to stable ID {travel_id}: "
                        f"{c(stable[1], Color.GREEN)} in "
                        f"{c(stable[3], Color.YELLOW)}, "
                        f"which is a {c(stable[2], Color.CYAN)} region."
                    )

                    # deduct travel cost
                    cursor.execute(
                        "UPDATE player_stats SET gold = gold - 40 WHERE save_id = %s;",
                        (save_id,)
                    )

                    # update player location
                    cursor.execute(
                        "UPDATE player_stats SET location = %s WHERE save_id = %s;",
                        (travel_id, save_id)
                    )

                    conn.commit()
                    cursor.close()

                    break

                else:
                    print(c("Invalid stable ID. Please try again.", Color.RED))

                cursor.close()

            break

        elif is_travel == "n":
            print("You chose not to travel.")
            break

        else:
            print(c("Invalid input. Please enter Y or N.", Color.RED))