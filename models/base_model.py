#!/usr/bin/python3
"""Base class Module
It defines all common attributes/methods for other classes
for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """The base model of object hierarchy class."""

    def __init__(self, *args, **kwargs):
        """The Base instance Initialization

        Args:
            - *args: list of arguments of the function
            - **kwargs: dict of key-values arguments of the function
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """For the instances, it returns a human-readable
        string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """It updates the attribute with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """A dict. representation of an instance it returns."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
