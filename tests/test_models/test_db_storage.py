#!/usr/bin/python3
""" Test cases for the database storage
"""
import unittest
import os
import json
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """ Test if  all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """ Test that all returns all rows when no class is passed"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """ Test that new adds an object to the database"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """ Test that save properly saves objects to file.json"""
