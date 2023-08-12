"""Test case for user class"""
import models
import unittest
from models.user import User
from models import BaseModel

class TestUser(unittest.TestCase):
    """Test case for user class"""
def test_inheritance(self):
        """test if class was able to innherit BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

def test_attr(self):
    """test if attributes were created """
    user = User()
    self.assertTrue(hasattr(user, "email"))
    self.assertTrue(hasattr(user, "password"))
    self.assertTrue(hasattr(user, "first_name"))
    self.assertTrue(hasattr(user, "last_name"))

def test_attr_value(self):
        """test if attribute value"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

def test_att_type(self):
        """test the type of value"""
        user = User()
        self.assertTrue(type(user.email) == str)
        self.assertTrue(type(user.password) == str)
        self.assertTrue(type(user.first_name) == str)
        self.assertTrue(type(user.last_name) == str)

if __name__ == "__main__":
    unittest.main()