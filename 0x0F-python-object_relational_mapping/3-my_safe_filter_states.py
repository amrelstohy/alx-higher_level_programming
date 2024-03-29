#!/usr/bin/python3
"""
python script that ---
"""

import sys

if __name__ == "__main__":
    import MySQLdb
    if (len(sys.argv) == 5):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        motif = sys.argv[4]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (motif,)
            )
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
