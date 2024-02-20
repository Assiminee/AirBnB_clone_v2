#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_type
from models.place import place_amenity
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """describes Amenity class"""
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities"
                                       )
    else:
        name = ""
