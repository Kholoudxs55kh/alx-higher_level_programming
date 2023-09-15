#!/usr/bin/python3
"""Safe from sql injection"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for rw in rows:
        print(rw)
    cur.close()
    db.close()
