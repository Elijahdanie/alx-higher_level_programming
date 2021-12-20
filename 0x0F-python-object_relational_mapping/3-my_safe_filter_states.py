#!/usr/bin/python3
"""
This module fetches the state record indicated by the
state name from the command line argument, eleminating
vulnerability for SQL injections. %s symbol lets
the entry get included seperately from the sql query as
a value type, rather than a string type
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                                passwd=sys.argv[1],
                                user=sys.argv[2],
                                db=sys.argv[3])
    cursor = conn.cursor()
    targetState = sys.argv[4]
    cursor.execute(
        "select * from states where name = %s order by id ASC",
        (sys.argv[4],))
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    conn.close()
