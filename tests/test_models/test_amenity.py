"""Test case for Amenity Module"""
import unittest
from models.amenity import Amenity
import models.amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test case for Amenity class"""
    def test_inheritance(self):
        """Testing if class has inherited from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """testing for clas attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))


if __name__ == '__main__':
    unittest.main()