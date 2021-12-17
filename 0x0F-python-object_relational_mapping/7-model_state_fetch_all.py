#!/usr/bin/python
"""
This module list all the states in the database using sqlalchemy
"""
import sys

from sqlalchemy.sql.functions import session_user
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    results = session.query(State).order_by(State.id).all()
    for state in results:
        print("{}: {}".format(state.id, state.name))
    session.close()
