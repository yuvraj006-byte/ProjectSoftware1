# inventory_store.py
# -----------------
# Handles displaying the player's inventory and interacting with the in-game store.

from inventory.inventory import get_inventory  # Function to fetch player's inventory from DB
from tabulate import tabulate         # Library for nicely formatted tables in terminal


# ----------------------------
# Terminal color codes
# ----------------------------
class Color:
    CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    GREEN = "\033[1;32m"
    MAGENTA = "\033[1;35m"
    BRIGHT_BLACK = "\033[1;30m"
    RED = "\033[1;31m"
    RESET = "\033[0m"  # Reset terminal color back to default


# ----------------------------
# Color formatting helper
# ----------------------------
def c(text, color):
    """Wrap text with ANSI color codes for terminal output."""
    return f"{color}{text}{Color.RESET}"


# ----------------------------
# Display player's inventory
# ----------------------------
def display_inventory(inventory):
    if not inventory:
        print(c("Your inventory is empty.", Color.RED))
        return None

    table_data = []

    for item in inventory:
        table_data.append([
            c(str(item["item_id"]), Color.YELLOW),       # Item ID in yellow
            c(item["item_name"], Color.GREEN),           # Item name in green
            c(item["item_type"], Color.CYAN),            # Type in cyan
            c(str(item["quantity"]), Color.MAGENTA),     # Quantity in magenta
            c(str(item["equipped"]), Color.RED),         # Equipped status in red
            c(str(item["value_in_gold"]), Color.YELLOW), # Value in gold in yellow
        ])

    headers = [
        "ID",
        "Item Name",
        "Type",
        "Qty",
        "Equipped",
        "Value (Gold)"
    ]

    # Print formatted table
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    return int(item["value_in_gold"])

# ----------------------------
# Display items available in the store
# ----------------------------
def display_store_items(conn):
    cursor = conn.cursor(buffered=True)
    cursor.execute(
        "SELECT id, item_name, item_type, value_in_gold FROM items WHERE item_type != 'Shields';"
    )
    items = cursor.fetchall()

    if not items:
        print(c("Store is empty.", Color.RED))
        return

    table_data = []

    for item in items:
        table_data.append([
            c(str(item[0]), Color.YELLOW),  # Item ID
            c(item[1], Color.GREEN),        # Name
            c(item[2], Color.CYAN),         # Type
            c(str(item[3]), Color.YELLOW),  # Price
        ])

    headers = ["ID", "Item Name", "Type", "Price (Gold)"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


# ----------------------------
# Main store interaction loop
# ----------------------------
def store(conn, save_id):
    while True:
        choice = input("\nDo You Want To Sell Or Buy (`S` / `B`) Items? Type `Q` to Quit: ").strip().lower()

        # ----------------------------
        # Sell items
        # ----------------------------
        if choice == "s":
            inventory = get_inventory(conn, save_id)  # Fetch player's inventory
            value_in_gold = display_inventory(inventory)

            if not inventory:
                continue

            valid_ids = [str(item["item_id"]) for item in inventory]

            sell_choice = input("Enter the Item ID you want to sell (or Q to cancel): ").strip().lower()

            if sell_choice == "q":
                continue

            if sell_choice not in valid_ids:
                print(c("Invalid item ID.", Color.RED))
                continue

            # Confirm the sale
            confirm = input("Confirm sale by re-entering the Item ID: ").strip().lower()
            if confirm != sell_choice:
                print(c("Item IDs did not match. Sale cancelled.", Color.RED))
                continue

            # ----------------------------
            # Get current quantity of the item
            # ----------------------------
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute(
                "SELECT quantity, value_in_gold FROM inventory JOIN items ON inventory.item_id = items.id WHERE save_id = %s AND item_id = %s;",
                (save_id, sell_choice)
            )
            item_row = cursor.fetchone()

            if not item_row:
                print(c("Item not found in inventory.", Color.RED))
                continue

            current_qty = item_row["quantity"]
            value_in_gold = item_row["value_in_gold"]

            # ----------------------------
            # If quantity > 1, decrease it; otherwise, delete the item
            # ----------------------------
            if current_qty > 1:
                cursor.execute(
                    "UPDATE inventory SET quantity = quantity - 1 WHERE save_id = %s AND item_id = %s;",
                    (save_id, sell_choice)
                )
            else:
                cursor.execute(
                    "DELETE FROM inventory WHERE save_id = %s AND item_id = %s;",
                    (save_id, sell_choice)
                )

            # Add gold to player
            cursor.execute(
                "UPDATE player_stats SET gold = gold + %s WHERE save_id = %s;",
                (value_in_gold, save_id)
            )
            conn.commit()

            print(c("Item sold successfully!", Color.GREEN))

        # ----------------------------
        # Buy items
        # ----------------------------
        elif choice == "b":
            display_store_items(conn)  # Show all available store items

            buy_choice = input("Enter the Item ID you want to buy (or Q to cancel): ").strip().lower()

            if buy_choice == "q":
                continue  # Go back to main store menu

            # ----------------------------
            # Fetch the selected item's details
            # ----------------------------
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute(
                "SELECT item_name, value_in_gold FROM items WHERE id = %s;",
                (buy_choice,)
            )
            item = cursor.fetchone()

            if not item:
                print(c("Invalid item ID.", Color.RED))
                continue

            # Confirm the purchase
            confirm = input("Confirm purchase by re-entering the Item ID: ").strip().lower()
            if confirm != buy_choice:
                print(c("Item IDs did not match. Purchase cancelled.", Color.RED))
                continue

            # Set quantity to 1 by default
            quantity = 1
            value_in_gold = item["value_in_gold"]

            # ----------------------------
            # Deduct gold from player
            # ----------------------------

            cursor.execute(
                "SELECT gold FROM player_stats WHERE save_id = %s;", 
                (save_id,)
            )
            player_gold = cursor.fetchone()["gold"]

            if player_gold < value_in_gold:
                print(c("Not enough gold to buy this item.", Color.RED))
                continue

            # Deduct gold
            cursor.execute(
                "UPDATE player_stats SET gold = gold - %s WHERE save_id = %s;", 
                (value_in_gold, save_id)
            )

            # ----------------------------
            # Add item to inventory
            # ----------------------------
            cursor.execute(
                """
                INSERT INTO inventory (save_id, item_id, quantity, equipped)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    quantity = quantity + VALUES(quantity);
                """,
                (save_id, buy_choice, quantity, False)
            )
            conn.commit()

            print(c(f"Purchased {item['item_name']} for {value_in_gold} gold!", Color.GREEN))
        # ----------------------------
        # Exit store
        # ----------------------------
        elif choice == "q":
            print(c("Exiting Store!", Color.MAGENTA))
            break

        # ----------------------------
        # Invalid input
        # ----------------------------
        else:
            print(c("Invalid choice. Please enter S, B, or Q.", Color.RED))