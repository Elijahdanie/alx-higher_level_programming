#!/usr/bin/python3
"""
This module represents the City Object of the City table
In the database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
