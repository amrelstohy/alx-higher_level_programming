#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name, \
            (SELECT name FROM states WHERE id = state_id)\
                 FROM cities ORDER BY id ASC")
    x = cur.fetchall()
    for i in x:
        print(i)