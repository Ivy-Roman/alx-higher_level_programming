#!/usr/bin/python3
"""
return all state objects from database via python
parameters given to script: username, password, database
"""

from sys import argv
from model_state import State
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
    state = session.query(State).filter(
        State.name.like('%a%')).all()
    for s in state:
        session.delete(s)

    session.commit()

    session.close()
