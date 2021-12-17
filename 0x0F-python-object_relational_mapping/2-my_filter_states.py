#!/usr/bin/python3
"""
This module fetches the state record from database
using name indicated in the command line argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                                passwd=sys.argv[1],
                                user=sys.argv[2],
                                db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("select * from states where name = '{}' order by id ASC".format(sys.argv[4]))
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    conn.close()
