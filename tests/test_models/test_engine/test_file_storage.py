#!/usr/bin/env python3
"""Test case for file storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import models.engine.file_storage


class TestFileStorage(unittest.TestCase):
    """testcases for file storage methods"""
    __file_path = "file.json"

    def test_attr(self):
        """test if attributes created"""
        file_store = FileStorage()
        self.assertIsInstance(file_store, FileStorage)
        self.assertTrue(hasattr(file_store, "__file_path"))
        self.assertTrue(hasattr(file_store, "__objects"))

    def test_attr_type(self):
        """test attribute type"""
        file_store = FileStorage()
        self.assertTrue(type(file_store.__file_path) == str)
        self.assertTrue(type(file_store.__objects) == dict)

    def test_all(self):
        """Test the all method"""
        all_instance = self.storage.all()
        self.assertIsInstance(all_instance, dict)
        self.assertIs(all_instance, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()