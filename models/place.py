#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base, storage_type
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == "db":
        # Foreign keys
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

        # Table specific columns
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        # Relationship
        reviews = relationship("Review",
                               cascade="all, delete-orphan",
                               backref="places")

        # Association table: many-to-many relationship
        place_amenity = Table("place_amenity", Base.metadata,
                              Column(
                                  String(60),
                                  ForeignKey("places.id"),
                                  primary_key=True,
                                  nullable=False
                                  ),
                              Column(
                                  String(60),
                                  ForeignKey("amenities.id"),
                                  primary_key=True,
                                  nullable=False
                                  )
                              )

        # Relationship
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates="place_amenities"
                                )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns a list of reviews where the place id
            matches that of the current instance
            """
            reviews_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.place_id:
                    reviews_list.append(review)
            return reviews_list
