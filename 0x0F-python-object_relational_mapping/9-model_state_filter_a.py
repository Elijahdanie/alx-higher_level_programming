#!usr/bin/python3
"""
This module fetches states that contains the letter 'a'
from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
    format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    results = session.query(State).filter(
        State.name.contains('a%')).order_by(
        State.id).all()
    for result in results:
        print('{}: {}'.format(result.id, result.name))
    session.close()
