#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
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
    data = session.query(State).order_by(State.id).all()
    for i in data:
        print("{}: {}".format(i.id, i.name))
