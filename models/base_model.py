#!/usr/bin/python3
'''
This is a base model that defines all common attributes and
methods of other classes
'''
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    '''
    represents the base model class of AirBnB console
    '''

    def __init__(self, *args, **kwargs):
        '''
        constructor
        '''

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for i, j in kwargs.items():
                if "__class__" not in i:
                    setattr(self, i, j)

    def __str__(self):
        """string representation of an instance """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        update public update at current time instance
        '''
        self.updated_at = datetime.now()
        model.storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictionary['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dictionary