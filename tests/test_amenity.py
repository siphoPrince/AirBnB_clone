import unittest
from models.amenity import Amenity



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

    def test_initialization(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_to_dict(self):
        amenity = Amenity(name="Pool")
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Pool")

if __name__ == '__main__':
    unittest.main()

