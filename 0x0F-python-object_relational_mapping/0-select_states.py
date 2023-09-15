#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb


def close_db(db):
    """to close all at once
    and to be reusable"""
    curr = db.cursor()
    db.close()
    curr.close()


if __name__ == '__main__':

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    cur.excute('SELECT * from states')

    for rw in cur.fetchall():
        print(rw)

    close_db(conn)
