from auth.logIn import log_in
from auth.signUp import sign_up

# Wrapper function for login
def try_login(conn):
    user_id = log_in(conn)
    return user_id

# Wrapper function for signup
def try_sign_up(conn):
    success = sign_up(conn)
    return success