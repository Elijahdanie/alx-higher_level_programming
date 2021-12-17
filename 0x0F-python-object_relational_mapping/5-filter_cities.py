#!/usr/bin/python3
"""
This module fetches states and cities record
where name of state equal in the indicated commandline
argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                                passwd=sys.argv[1],
                                user=sys.argv[2],
                                db=sys.argv[3])
    cursor = conn.cursor()
    target_state = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON " +
                    "states.id = cities.state_id WHERE states.name = %s",
                    (target_state,))
    result = cursor.fetchall()
    values = ''
    for i in result:
        for j in i:
            values +=j + ', '
    print(values[:-2])
    cursor.close()
    conn.close()
