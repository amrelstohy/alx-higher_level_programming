#!/usr/bin/python3

"""
you turn the lights in then you get them back off
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states JOIN cities ON"
                " cities.state_id = states.id WHERE states.name = %s"
                " ORDER BY cities.id ASC", (state_name,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    if cities:
        print(', '.join(cities))
    else:
        print()
    cur.close()
    db.close()
