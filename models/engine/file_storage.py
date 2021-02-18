#!/usr/bin/python3
""" Import the modules need it for this storage """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ public instance return dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ public instance that sets in __objects """
        key = type(obj).__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Public instance that serializes __objects """
        d = {}
        with open(self.__file_path, 'w+') as f:
            for k, v in self.__objects.items():
                d[k] = v.to_dict()
            json.dump(d, f)

    def reload(self):
        """deserializes JSON to object"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
        except FileNotFoundError:
            return
        new_dct = {}
        for key, val in new_obj.items():
            new_dct[key] = eval(val["__class__"])(**val)
        self.__objects = new_dct
