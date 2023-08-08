#!/usr/bin/python3
from datetime import datetime
import uuid

'''
This is a base model that defines all common attributes and
methods of other classes
'''

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
            self.creted_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%M-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%M-%dT%H:%M:%S.%f')
    
    def __str__(self):
        """string representation of an object"""
        return "[{s}] ({s}) {s}" .format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat
        dictionary['updated_at'] = dictionary['updated_at'].isoformat

        return dictionary
            
    def save(self):
        '''
        update public update at current time instance
        '''
        self.updated_at = datetime.now()
        storage,save
