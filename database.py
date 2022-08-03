import mysql.connector

def connection(user="root", password="", host="localhost", database="practice_flask_rest_api_mysql_simple"):
    connect = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database,
    )
    return connect