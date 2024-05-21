import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        port='3312',
        database='duothan',
        user='root',
        password=''
    )
    return connection
