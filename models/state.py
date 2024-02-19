#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.__init__ import storage
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City",
                          cascade="all, delete-orphan",
                          backref="state")

    #name = ""
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns the list of City instances
            where state_id is equal to the current
            instance's State.id
            """
            cities_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.state_id:
                    cities_list.append(city)
            return cities_list

