#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def select_stetes():
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    select_stetes()
