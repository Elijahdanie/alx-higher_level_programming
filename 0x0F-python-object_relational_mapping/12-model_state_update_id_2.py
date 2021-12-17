#!/usr/bin/python3
"""
This module updates state at id 2 to 'New Mexico'
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
    format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    state_obj = session.query(State).filter(State.id == 2).one()
    state_obj.name = 'New Mexico'
    session.commit()
    session.close()
