import unittest
from models.amenity import Amenity
import models.amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    #def test_initialization(self):
        #amenity = Amenity(name="WiFi")
       # self.assertEqual(amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()

