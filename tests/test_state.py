"""Test case for State class"""
import unittest
import models
from models.state import State
from models import BaseModel

class TestState(unittest, TestCase):
    """Test case for state classes """
    def test_inheritance(self):
        """to test whether it inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "update_at"))

    def test_attributtes(self):
        """to test whether attributes are present"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        """test to dict method on state"""
        state = State()
        self.assertEqual(type(state.to_dict), dict)
        
if __name__ == "__main__":
    unittest.main()