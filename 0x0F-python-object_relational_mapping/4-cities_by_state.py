#!/usr/bin/python3
"""
This module fecthes states and cities records from
the database using the foreign key relationship 
cities.state_id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                                passwd=sys.argv[1],
                                user=sys.argv[2],
                                db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities " +
                        "INNER JOIN states ON states.id = cities.state_id order by id ASC")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    conn.close()
