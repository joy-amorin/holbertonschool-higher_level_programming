#!/usr/bin/python3
"""ists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def select_states():
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    select_states()