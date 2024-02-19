#!/usr/bin/python3
"""Defines the Database storage class
"""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    classes = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        """Initializes a database connection
        """
        # Information required for connection
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        database = getenv("HBNB_MYSQL_DB")

        database_auth = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, database)

        # Creating the engine
        self.__engine = create_engine(database_auth, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Uses the current database session to query the
        database for all instances of cls"""
        results = {}
        tables = [cls] if cls else classes
        for table in tables:
            cls_results = session.query(table).all()

            for res in cls_results:
                key = cls.__name__ + "." + res.id
                results[key] = res

        session.close()
        return results

    def new(self, obj):
        """adds a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session
        obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
