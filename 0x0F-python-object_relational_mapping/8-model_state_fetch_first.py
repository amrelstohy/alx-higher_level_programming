#!/usr/bin/python3
"""
python script that ---
"""

import re
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], str(sys.argv[2]), sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
