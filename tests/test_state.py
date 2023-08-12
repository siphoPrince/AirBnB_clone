"""Test case for State class"""
import unittest
import models
from models.state import State
from models import BaseModel

class TestState(unittest.TestCase):
    """Test case for state classes """
    def test_inheritance(self):
        """to test whether it inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_attributtes(self):
        """to test whether attributes are present"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

        
if __name__ == "__main__":
    unittest.main()