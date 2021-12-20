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
    query1 = "SELECT cities.id, cities.name, states.name "
    query2 = "FROM cities INNER JOIN states ON "
    query3 = "states.id = cities.state_id order by id ASC"
    cursor.execute(query1 + query2 + query3)
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    conn.close()
