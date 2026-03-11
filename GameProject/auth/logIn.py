import bcrypt
import pwinput

def log_in(conn):

    def get_user_record(username): 
        cursor = conn.cursor()
        
        sql = "SELECT id, username, password_hash FROM users WHERE username=%s;"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        cursor.close()

        return result

    while True:  # Keep asking until successful login
        username = input("Enter a User Name: ")
        password = pwinput.pwinput("Enter a Password: ", mask='*')

        record = get_user_record(username)

        if record:
            user_id, stored_username, stored_hash = record

            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')

            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                return user_id

        print("Invalid username or password.\n")