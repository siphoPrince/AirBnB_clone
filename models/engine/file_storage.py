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

    __path = "JSONstorage.json"
    __objects = {}

    def save(self):
        '''
        converting data that is stored in a JSON
        back into its original structure
        '''

        my_dict = {}
        my_dict.update(FileStorage.__objects)
        for key, value in my_dict.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage._file_path, "w+") as write_file:
            json.dump(my_dict, write_file)

    def reload(self):
        '''
        if __path file exits the deserialize the json file
        If not then do nothing
        '''
        new_dict = {}
        try:
            from models.base_model import BaseModel
            with open(self.__path, "r") as read_file:
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

    def new(self, obj):
        '''
        sets __objects with key <obj class name>.id
        '''
        key = obj.to_dict()['__class__'] + "." + obj.id
        FileStorage.__objects.update({key:obj})
