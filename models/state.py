#!/usr/bin/python3

'''
State class
'''

from models.base_model import BaseModel

class State(BaseModel):
    '''
    State class inherits from BaseModel
    '''

    def __init__(self, *args, **kwargs):
        """
        Initialize State instance.

        Args:
            args: Arbitrary positional arguments.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ''

