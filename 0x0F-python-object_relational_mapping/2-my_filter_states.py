#!/usr/bin/python3
"""script that lists all states with a name starting with N"""

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
                 WHERE name LIKE BINARY '{}'\
                 ORDER BY id ASC".format(argv[4]))

    rows = cur.fetchall()
    for rw in rows:
        print(rw)

    cur.close()
    conn.close()
