import bcrypt
import pwinput

def sign_up(conn):

    def get_sign_up_details():
        user_name = input("Enter a User Name: ").strip()
        pws1 = pwinput.pwinput("Enter a Password: ", mask='*')
        pws2 = pwinput.pwinput("Confirm the Password: ", mask='*')
        return user_name, pws1, pws2

    def hash_password(password):
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt)

    def register_user(username, password):
        cursor = conn.cursor()

        # Check if username exists
        cursor.execute("SELECT id FROM users WHERE username=%s;", (username,))
        if cursor.fetchone():
            print("Username already taken. Please choose another.\n")
            cursor.close()
            return None

        # Insert and return user_id
        cursor.execute(
            "INSERT INTO users(username, password_hash) "
            "VALUES(%s, %s) RETURNING id;",
            (username, hash_password(password))
        )

        user_id = cursor.fetchone()[0]  # get the returned id
        conn.commit()
        cursor.close()
        return user_id

    print("\n=== Create Your Account ===\n")

    for _ in range(3):
        user_name, pws1, pws2 = get_sign_up_details()

        if not user_name:
            print("Username cannot be empty.\n")
            continue

        if len(pws1) < 6:
            print("Password must be at least 6 characters.\n")
            continue

        if pws1 != pws2:
            print("Passwords do NOT match. Please try again!\n")
            continue

        user_id = register_user(user_name, pws1)
        if user_id:
            print("\n✅ You Are Now Registered!")
            return user_id   # <-- return user_id instead of True

    print("❌ Failed to register account after multiple attempts.\n")
    return None