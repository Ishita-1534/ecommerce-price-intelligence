import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ishita@1534",
        database="book_price_intelligence"
    )

    return connection