#!/usr/bin/python3
"""
python script that ---
"""

import re
import sys
from unittest import result
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], str(sys.argv[2]), sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    req = select(State).where(State.name == '*a*')
    result = session.execute(req)
    if result is None:
        print("Nothing")
    else:
        i = 1
        for state_obj in result.scalars():
            print("{}: {}".format(i, state_obj.name))
            i += 1
