#!/usr/bin/python3
"""
 a script that prints all City objects from the database
 """
"""from model_state import Base, State """
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
        )
    session = Session(engine)
    data = session.query(City).order_by(City.id).all()
    for i in data:
        print("{}: ({}) {}".format(i.state.name, i.id, i.name))
    session.close()
