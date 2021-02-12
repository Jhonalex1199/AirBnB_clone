#!/usr/bin/python3
"""Basemodel of AirBnB"""
import uuid
import datetime


class BaseModel:
    """a documentation of my class:
    defines all common attributes/methods\
    for other classes:"""

    def __init__(self, id="", *args, **kwargs)):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.update_at = created_at

        if kwargs:
            

    def __str__(self):
        """string representation"""

        return '[{}]'.format(self.__class__.__name__) + '({})'.format(self.id) + '{}'.format(self.__dict__)
        
    def save(self):
        """ updates the public instance attribute updated_at"""

        self.update_at = datetime.datetime.now()
        return self.update_at

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        dict_a = self.__dict__
        dict_a["created_at"] = self.created_at.isoformat()
        dict_a["update_at"] = self.update_at.isoformat()
        dict_a["__class__"] = self.__class__.__name__
        return dict_a
