#!/usr/bin/python3
"""Base model"""
import uuid

class BaseModel():
    """ Base class for the AirBnB console
    defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialization of attributes"""
        self.id = str(uuid.uuid4())

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
