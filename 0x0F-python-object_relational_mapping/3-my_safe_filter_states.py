#!/usr/bin/python3
"""Safe from sql injection"""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE BINARY name = %s\
                 ORDER BY id ASC", (argv[4]))

    rows = cur.fetchall()
    for rw in rows:
        print(rw)

    cur.close()
    conn.close()
