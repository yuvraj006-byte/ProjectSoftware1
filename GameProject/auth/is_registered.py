from auth.auth_wrap import try_login as log_in, try_sign_up as sign_up  

def user_account(conn):
    while True:
        answer = input("Do You Have An Account? (Y/N)?: ").strip().lower()
        
        if answer == "y":
            print("Fantastic! You Can Use Your Credentials To Login!")
            return log_in(conn)
        elif answer == "n":
            print("Okay! Let's Create Your Account First!")
            return sign_up(conn)
        else:
            print("Invalid Input! Please Enter Y or N.\n")