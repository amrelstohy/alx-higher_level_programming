#!/usr/bin/python3
"""
you turn the lights in then you get them back off
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

base = declarative_base()


class State(base):
    """state class"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
        )
