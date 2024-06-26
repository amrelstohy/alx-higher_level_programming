#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the letter 'a'
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
    data = session.query(State).filter(State.name.like('%a%')).all()
    for i in data:
        session.delete(i)
    session.commit()
    session.close()
