import mysql.connector


# Connect to MySQL
def get_query():
    connection = mysql.connector.connect(
        host="db_host",
        port=3306,
        user="db_user",
        password="db_password",
        database="db_name"
    )
   
    return connection 