#!/usr/bin/python3
'''
serialized and deserialized instances to a json file
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''
    fillestorage class representation
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        returns all dictionary
        '''
        return self.__objects
        
    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id"""
        
        #key = obj.to_dict()['__class__'] + "." + obj.id
        key = "{}.{}".format(__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        '''
        converting python data to JSON
        data structure
        '''

        my_dict = {}
        for key, value in self.__objects.items():
            print(self.__objects)
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            json.dump(my_dict, write_file)

    def reload(self):
        '''
        Deserializes the JSON file to __objects (if the JSON file exists).
        If the file doesn't exist or any other error occurs, do nothing.
        '''
        try:
            with open(self.__file_path, "r") as read_file:
                data = json.load(read_file)
                print("data:{}".format( data))
                for key, value in data.items():
                    #if key not in self.__objects:
                     #   if value['__class__'] == 'User':
                    self.__objects[key] = BaseModel(**value)
                    #self.new(eval(key.split(".")[0])(**value))  
        except (FileNotFoundError, json.JSONDecodeError, TypeError):
            # Handle file not found, JSON decoding error, or unexpected value types
            pass

