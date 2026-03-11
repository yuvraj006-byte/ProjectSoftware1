import mysql.connector


# Connect to MySQL
def get_query():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="username",
        password="password",
        database="fantasy_game"
    )
   
    return connection 