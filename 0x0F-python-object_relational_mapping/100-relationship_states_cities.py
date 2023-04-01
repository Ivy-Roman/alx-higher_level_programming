#!/usr/bin/python3
"""
return all cities objects from database
parameters given to script: username, password, database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query python instances in database
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_city)
    session.add(new_state)
    session.commit()

    session.close()
