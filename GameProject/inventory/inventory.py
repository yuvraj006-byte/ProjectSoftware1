def save_inventory(conn, save_id, item_id, quantity, equipped):
    cursor = conn.cursor(buffered=True)
    query = """
        INSERT INTO inventory (save_id, item_id, quantity, equipped)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        quantity = quantity + VALUES(quantity),
        equipped = VALUES(equipped);
    """
    cursor.execute(query, (save_id, item_id, quantity, equipped))
    conn.commit()
    cursor.close()
    
def get_inventory(conn, save_id):
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT items.item_name, items.item_type, inventory.quantity, inventory.equipped, items.value_in_gold, inventory.item_id
        FROM inventory
        JOIN items ON inventory.item_id = items.id
        WHERE inventory.save_id = %s
    """
    cursor.execute(query, (save_id,))
    inventory = cursor.fetchall()
    cursor.close()
    return inventory