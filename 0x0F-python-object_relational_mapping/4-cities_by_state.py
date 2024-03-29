#!/usr/bin/python3
"""
python script that ---
"""

import sys

if __name__ == "__main__":
    import MySQLdb
    if (len(sys.argv) == 4):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT id, name, \
            (SELECT name FROM states WHERE id = state_id)\
                 FROM cities ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
