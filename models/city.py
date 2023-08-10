#!/usr/bin/python3

'''
City class
'''

from models.base_model import BaseModel

class City(BaseModel):
    '''
    City class inherits from BaseModel
    '''

    def __init__(self, *args, **kwargs):
        """
        Initialize City instance.

        Args:
            args: Arbitrary positional arguments.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ''
        self.name = ''

