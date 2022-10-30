import re
import sqlite3
import os
import random


def get_db_connection():
    connection = sqlite3.connect("src" + os.sep + "Hafez.db")
    return connection
  
def start():
    connection = get_db_connection()
    selected_poem = random.randint(0,415)
    query = "SELECT TEXT FROM poems WHERE id = " + str(selected_poem)
    cur = connection.cursor()
    cur.execute(query)
    poem = cur.fetchone()[0]
    print(poem)

start()