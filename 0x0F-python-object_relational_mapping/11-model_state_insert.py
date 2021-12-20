#!/usr/bin/python3
"""
This module adds a state nameed 'Louisiana' to the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    obj = State()
    obj.name = 'Louisiana'
    session.add(obj)
    session.commit()
    print(obj.id)
    session.close()
