"""Test case for Review Class"""
import models
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Test case for Review Class"""
    def test_inheritance(self):
        """test if class was able to innherit BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_attr(self):
        """test if attributes were created """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_attr_value(self):
        """test if attribute value"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def tst_att_type(self):
        """test the type of value"""
        review = Review()
        self.assertTrue(type(review.place_id) == str)
        self.assertTrue(type(review.user_id) == str)
        self.assertTrue(type(review.text) == str)

if __name__ == "__main__":
    unittest.main()