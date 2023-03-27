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
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM states
                   INNER JOIN cities ON states.id = cities.state_id
                   ORDER BY id ASC""")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
