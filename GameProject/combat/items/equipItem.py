def pause():
    input('\033[32mPress Enter to continue...\033[0m')


def equip_item(conn, save_id):
    cursor = conn.cursor(buffered=True)

    # Show inventory once
    cursor.execute("""
        SELECT inventory.item_id,
               items.item_name,
               items.item_type,
               inventory.quantity,
               inventory.equipped
        FROM inventory
        JOIN items ON inventory.item_id = items.id
        WHERE inventory.save_id = %s
    """, (save_id,))
    show_inventory = cursor.fetchall()

    if not show_inventory:
        print("Your inventory is empty.")
        pause()
        cursor.close()
        return None

    print("\n===== YOUR INVENTORY =====")
    print(f"{'ID':<5} {'NAME':<30} {'TYPE':<15} {'QTY':<5} {'EQUIPPED':<10}")
    print("-" * 60)
    for item in show_inventory:
        item_id, name, item_type, quantity, equipped = item
        equipped_str = "Yes" if equipped else "No"
        print(f"{item_id:<5} {name:<30} {item_type:<15} {quantity:<5} {equipped_str:<10}")
    print("-" * 60)

    # Loop to equip multiple items
    while True:
        equip_choice = input("Enter the item ID to equip (or 'q' to finish): ").strip().lower()
        if equip_choice in ('q', 'quit', 'done'):
            print("Finished equipping items.")
            break

        # Validate selection
        valid_ids = [str(row[0]) for row in show_inventory]
        if equip_choice not in valid_ids:
            print("Invalid item ID. Try again.")
            continue

        # Get item type
        cursor.execute("SELECT item_type FROM items WHERE id = %s", (equip_choice,))
        result = cursor.fetchone()
        if not result:
            print("Error fetching item type.")
            continue
        item_type = result[0]

        # Unequip currently equipped item of same type
        cursor.execute("""
            UPDATE inventory
            SET equipped = FALSE
            WHERE save_id = %s
              AND item_id IN (
                  SELECT id FROM items WHERE item_type = %s
              )
        """, (save_id, item_type))

        # Equip selected item
        cursor.execute("""
            UPDATE inventory
            SET equipped = TRUE
            WHERE item_id = %s
              AND save_id = %s
        """, (equip_choice, save_id))

        conn.commit()
        print(f"✅ Equipped item successfully!")

    cursor.close()
    pause()
    return None