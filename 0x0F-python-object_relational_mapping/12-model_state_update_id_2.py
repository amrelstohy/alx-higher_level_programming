#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
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
    data = session.query(State).filter(State.id == 2).first()
    data.name = "New Mexico"
    session.commit()
    session.close()
