#!/usr/bin/python3
"""Basemodel of AirBnB"""
import uuid
from datetime import datetime
import json


class BaseModel:
    """defines all common attributes/methods for other classes:"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "update_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            from models.__init__ import storage
            storage.new(self)

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.update_at = datetime.now()
        from models.__init__ import storage
        storage.new(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values\
        of __dict__ of the instance"""
        dict_a = self.__dict__
        dict_a["created_at"] = self.created_at.isoformat()
        dict_a["update_at"] = self.update_at.isoformat()
        dict_a["__class__"] = self.__class__.__name__
        return dict_a
