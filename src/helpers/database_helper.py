import sqlite3
import os

def get_db_connection():
    connection = sqlite3.connect("/home/admin/Hamraham-bot/src" + os.sep + "Hafez.db")
    return connection

def get_all_poems():
    connection = get_db_connection()
    query = "SELECT TEXT FROM poems"
    cur = connection.cursor()
    cur.execute(query)
    poems = cur.fetchall()
    return poems


