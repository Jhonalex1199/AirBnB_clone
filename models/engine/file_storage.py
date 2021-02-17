#!/usr/bin/python3
"""Storage"""
import json
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and\
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key obj.id"""
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except Exception:
            pass
