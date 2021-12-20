#!/usr/bin/python3
""" This module, list all the cities joined by their states"""


import sys
from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    result = session.query(State, City).join(City).order_by(City.id)
    for row in result:
        state, city = row
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
