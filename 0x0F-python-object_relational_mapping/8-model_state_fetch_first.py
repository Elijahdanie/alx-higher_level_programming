#!/usr/bin/python3

"""
This Module fetches the first record of states in the
database using sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    session = sessionmaker(engine)()
    results = session.query(State).order_by(State.id).first()
    if results is not None:
        print('{}: {}'.format(results.id, results.name))
    session.close()
