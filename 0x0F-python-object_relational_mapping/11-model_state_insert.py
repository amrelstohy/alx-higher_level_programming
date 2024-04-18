#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database
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
    new = State(name = "Louisiana")
    x = session.add(new)
    print(x.id)
