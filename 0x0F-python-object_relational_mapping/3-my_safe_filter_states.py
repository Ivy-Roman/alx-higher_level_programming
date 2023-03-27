#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # create cursor to execute queries
    # using SQL
    cur = db.cursor()
    sql_cmd = """SELECT * FROM states WHERE name =%s
                 ORDER BY id ASC"""
    cur.execute(sql_cmd, (argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
