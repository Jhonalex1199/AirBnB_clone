#!/usr/bin/python3
"""Unittest module for the class BaseModel
"""
import os
import unittest
import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """methods of the test for class BaseModel
    """
    def test_documentation(self):
        """this checks all the documentation
        of all the methods of the BaseModel class
        """
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_uniqueId(self):
        """this check if the instance
        that are created has a unique id
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)
        self.assertNotEqual(instance1.id, instance2.id)

    def test_exec_permissions(self):
        """Method that review if the file is executable
        """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exect)

    def test_typeData(self):
        """this method check the type of
        the atributes when created a instance
        """
        instance1 = BaseModel()
        self.assertIsInstance(instance1.created_at, datetime.datetime)
        self.assertIsInstance(instance1.updated_at, datetime.datetime)
        self.assertIsInstance(instance1.id, str)
        self.assertIsInstance(instance1, BaseModel)

if __name__ == '__main__':
    unittest.main()
