#!/usr/bin/python3
"""
This module selects all states that begin with the letter 'N'
and orders in ascending order
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                                passwd=sys.argv[1],
                                user=sys.argv[2],
                                db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("select * from states where name like 'N%' order by id ASC")
    results = cursor.fetchall()
    for i in results:
        print(i)
    cursor.close()
    conn.close()
