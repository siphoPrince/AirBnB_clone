"""Test for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""
    def test_attributes(self):
        """Test for BaseModel attributes"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_id_generation(self):
        """Test for BaseModel id generation"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_created_at(self):
        """Test for BaseModel time"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at(self):
        """Test for BaseModel time"""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict(self):
        """Test for BaseModel to create dictionary"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_from_dict(self):
        """testing to extract from dict"""
        base_model_data = {
            '__class__': 'BaseModel',
            'id': '1234',
            'created_at': '2023-08-10T12:34:56.789012',
            'updated_at': '2023-08-11T01:23:45.678901'
        }
        base_model = BaseModel(**base_model_data)
        self.assertEqual(base_model.id, '1234')
        self.assertEqual(base_model.created_at, datetime(2023, 8, 10, 12, 34, 56, 789012))
        self.assertEqual(base_model.updated_at, datetime(2023, 8, 11, 1, 23, 45, 678901))

        def test_save(self, mock_storage):
            """
             test save and update at is working and storage call
               save
            """
            base_model = BaseModel()
            old_created = base_model.created_at
            old_update = base_model.updated_at
            base_model.save()
            new_created = base_model.created_at
            new_updated = base_model.updated_at
            self.assertNotEqual(old_update, new_updated)
            self.assertEqual(old_created, new_created)
            self.assertEqual(base_model.updated_at, datetime.now())


if __name__ == '__main__':
    unittest.main()