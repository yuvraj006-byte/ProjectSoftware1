from tabulate import tabulate
import playerUI.playerUI as playerUI
from getQuery.getQuery import get_query
from gameState.loadGame import load_game
from auth.is_registered import user_account
from gameState.newSave import create_new_save
from inventory.inventory import save_inventory
from gameText.openingScene import opening_scene
from items.firstItems import get_random_loadout
from gameMenu.menu import game_menu, menu_result
from position.firstRandomStable import get_first_random_stable 
from butlerUI.butlerUI import butler_1, butler_2, butler_5, butler_6, butler_7, butler_8, butler_9

def pause():
    input('\033[32mPress Enter to continue...\033[0m') 

# ------------------ MAIN ------------------
conn = get_query()  # DB connection

def main():
    try:
        print("Welcome To \033[96mDemonic Invasion\033[0m")

        # ---------------- LOGIN / SIGNUP ----------------
        user_id = user_account(conn)
        if user_id is None:
            print("Exiting game due to failed login/signup.")
            conn.close()
            return
        print()

        butler_1()

         # ---------------- WORLD HISTORY ----------------
        while True:
            world_history_choice = input("Type Here: ").strip().lower()
            if world_history_choice == 'history':
                playerUI.world_history()
                pause()
                break
            elif world_history_choice == 'no':
                break
            else:
                print("Invalid Choice! Please Type 'History' OR 'No'!")        
        print()

        butler_5()
        print()
        # ---------------- SAVE SELECTION ----------------

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM game_saves WHERE user_id = %s;", (user_id,))
        saved_games = cursor.fetchall()

        if saved_games:
        # Get column names
            headers = [desc[0] for desc in cursor.description]

            print()
            print("\033[1;94mExisting Saved Games:\033[0m")
            print(tabulate(saved_games, headers=headers, tablefmt="grid"))
        else:
            print("No saves found.")

        save_choice = input("Enter save number to load, or type 'new' to create a new save: ").strip().lower()
        
        # ---------------- LOAD OR CREATE SAVE ----------------

        if save_choice == 'new':
            save_name = input("Enter the name of the Save: ").strip()    

            print()
            butler_8()

            first_stable_id, region = get_first_random_stable(conn)

            save_id = create_new_save(conn, user_id, save_name, first_stable_id)

            butler_9()
            print()

            item, item_id = get_random_loadout(conn, region)

            for key, value in item.items():
                print(f"{key.capitalize()}: {value}")
            pause()

            if item_id:
                save_inventory(conn, save_id, item_id, 1, False)

            opening_scene()
            pause()
            print()

            butler_6()  
            pause()

            butler_2()
            pause()
            print()

        else:
            save_id = int(input("Please Re-Enter The Save Id to load: ").strip())
            
            butler_7()

            cursor = conn.cursor(buffered=True)
            cursor.execute(
                "SELECT id FROM game_saves WHERE user_id = %s AND id = %s",
                (user_id, save_id)
            )
            result = cursor.fetchone()
            cursor.close()

            if not result:
                print(f"No save found with ID {save_id} for your account.")
                conn.close()
                return


        # ---------------- LOAD FULL GAME STATE ----------------

        stats, inventory, quests = load_game(conn, save_id)

        player_health = stats["health"]
        
        # -------------- MAIN GAME LOOP --------------
        while True:
            choice = game_menu()
            player_health = menu_result(conn, save_id, choice, player_health)

    finally:
        conn.close()

# ------------------ RUN GAME -----------------
main()

