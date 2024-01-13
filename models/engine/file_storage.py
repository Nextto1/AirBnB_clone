#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Various class for serializtion and deserialization
    of the base classes for the fucntion."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """It returns __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """It sets new objects in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """It serializes __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {e: v.to_dict() for e, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """It returns a dictionary of accurate
        classes with their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """It deserializes the JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {e: self.classes()[v["__class__"]](**v)
                        for e, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """It returns the accurate attributes with
        their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
