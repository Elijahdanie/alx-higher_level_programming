#!/usr/bin/python3
""" This module selects all states ordered by states.id in
Ascending order """

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                                passwd=sys.argv[1],
                                user=sys.argv[2],
                                db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result = cursor.fetchall()
    for entries in result:
        print(entries)
    cursor.close()
    conn.close()
