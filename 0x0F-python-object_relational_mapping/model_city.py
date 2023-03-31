#!/usr/bin/python3
"""
Defines a state model
Inherits from SQLAlchemy Base and links to the MySQL table cities
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Represents a city for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store cities.
    id (sqlalchemy.Integer): The cities' id.
    name (sqlalchemy.String): The cities' name.
    """

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id),nullable=False)
