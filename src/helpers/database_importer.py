from msilib.schema import Error
import re
import sqlite3

file = open("Hafez.txt", "r", errors="ignore", encoding="utf8")
text = file.read()
replaced = re.sub(r"(غزل   *[۰-۹]*[۰-۹]*[۰-۹])", "---", text)
of = open("tex.txt", "w", errors="ignore", encoding="utf8")

try:
    con = sqlite3.connect("D:\Hafez Telegram Bot\src\Hafez.db")
    cur = con.cursor()
    splited = replaced.split("---")
    splited.pop(0)
    for item in splited:
        query = "INSERT INTO poems VALUES( NULL ,'" + item + "')"
        cur.execute(query)
        con.commit()
except sqlite3.Error as error:
    print(error)


of.write(replaced)
of.close()