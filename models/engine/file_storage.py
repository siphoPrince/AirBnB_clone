#!/usr/bin/python3
'''
serialized and deserialized instances to a json file
'''

import json
from datetime import datetime


class FileStorage:
    '''
    fillestorage class representation
    '''

    __file_path = "JSONstorage.json"
    __objects = {}

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
        for key in self.__objects:
            my_dict[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w+") as write_file:
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

    def all(self):
        '''
        returns all dictionary
        '''
        return FileStorage.__objects

#    def new(self, obj):
        '''
   #     sets __objects with key <obj class name>.id
        '''
  #      key = obj.to_dict()['__class__'] + "." + obj.id
 #       FileStorage.__objects.update({key:obj})
