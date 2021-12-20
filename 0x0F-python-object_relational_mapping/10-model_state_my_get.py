#!/usr/bin/python3

"""
This Module fetches a State record from database
using the indicated commandline argument also elimitnating
vulnerability for SQL injection
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
    result = session.query(State).order_by(State.id)
    found_result = False
    for i in result:
        if i.name == sys.argv[4]:
            print(i.id)
            found_result = True
            break
    if not found_result:
        print('Not Found')
