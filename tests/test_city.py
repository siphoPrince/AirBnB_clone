"""Test case for City Model"""
import unittest
from models.city import  City
from models import BaseModel

class TestCity(unittest.TestCase):
    """unittest for city class"""
    
    def test_Inheritance(self):
        """test if City class inherits from BaseModel"""

        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))



    def test_Attribute(self):
        """test for attribute"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

   
if __name__ == "__main__":
    unittest.main()       