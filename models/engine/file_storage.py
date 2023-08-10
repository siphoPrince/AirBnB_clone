#!/usr/bin/python3
'''
serialized and deserialized instances to a json file
'''
from models.base_model import BaseModel
import json
from datetime import datetime


class FileStorage:
    '''
    fillestorage class representation
    '''

    __file_path = "JSONstorage.json"
    __objects = {}

    def all(self):
        '''
        returns all dictionary
        '''
        return self.__objects
        
    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id"""
        
        key = obj.to_dict()['__class__'] + "." + obj.id
        self.__objects[key] = obj
    
    def save(self):
        '''
        converting python data to JSON
        data structure
        '''

        my_dict = {}
        for key, value in self.__objects.items():
            if isinstance(value, BaseModel):
                my_dict[key] = value.to_dict()
            else:
                 print(f"Object {value} is not an instance of BaseModel.")

        with open(self.__file_path, "w") as write_file:
            json.dump(my_dict, write_file)

    def reload(self):
        '''
        if __path file exits the deserialize the json file
        If not then do nothing
        '''
        new_dict = {}
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, "r") as read_file:
                new_dict = json.load(read_file)
                for key, value in new_dict.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except IOError:
            pass
