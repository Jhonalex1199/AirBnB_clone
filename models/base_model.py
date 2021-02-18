#!/usr/bin/pyhton3
"""Let's import the modules"""
import uuid
from datetime import datetime
import models
format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel():
    """class defines all common attributes/methods and the
    assign various atributes principal
    that should tener each object
    """

    def __init__(self, *args, **kwargs):
        '''inicialization Base
        *args won’t be used
        if kwargs is not empty:
        each key of this dictionary is an attribute name
        each value of this dictionary is the value of this attribute name
        '''
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
                if k == "created_at" or k == "updated_at":
                    form = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, k, datetime.datetime.strptime(v, form))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''human readable'''
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        creates dictionary of the class  and returns
        a dictionary of all the key values in __dict__
        '''
        dic2 = self.__dict__.copy()
        dic2["created_at"] = dic2["created_at"].isoformat()
        dic2["updated_at"] = dic2["updated_at"].isoformat()
        dic2["__class__"] = self.__class__.__name__

        return dic2

    def reload(self):
        """ deserialize the file json
        with load y and returns to make
        a update with all objects
        """
        filename = FileStorage.__file_path
        if path.exists(filename):
            with open(filename, "r") as f:
                load = json.load(f)
            for k, v in load.items():
                suma = eval(v["__class__"])(**v)
                FileStorage.__objects[k] = suma
