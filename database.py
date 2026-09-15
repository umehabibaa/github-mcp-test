import sqlite3


def get_connection():
    return sqlite3.connect("users.db")


def get_user(username):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT username, email, password FROM users WHERE username = ?",
        (username,)
    )

    row = cursor.fetchone()

    return {
        "username": row[0],
        "email": row[1],
        "password": row[2]
    } if row else None
