#!/usr/bin/python3

'''
Amenity class
'''

from models.base_model import BaseModel

class Amenity(BaseModel):
    '''
    Amenity class inherits from BaseModel
    '''

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity instance.

        Args:
            args: Arbitrary positional arguments.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ''
