#!/usr/bin/python3

'''
User class
'''

from models.base_model import BaseModel

class User(BaseModel):
    '''
    Class User inherits from BaseModel
    '''

    def __init__(self, email='', password='', first_name='', last_name='', **kwargs):
        """
        Initialize User instance.

        Args:
            email (str): User's email.
            password (str): User's password.
            first_name (str): User's first name.
            last_name (str): User's last name.
            kwargs: Additional keyword arguments passed to the parent class.
        """
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

