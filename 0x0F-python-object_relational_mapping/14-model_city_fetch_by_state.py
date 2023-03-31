#!/usr/bin/python3
"""
return all cities objects from database
parameters given to script: username, password, database
"""

from sys import argv
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query python instances in database
    for query in session.query(State.name, City.id, City.name).filter(State.id == City.state_id).order_by(City.id):
        print(f'{query[0]}: ({query[1]}) {query[2]}')

    session.close()
