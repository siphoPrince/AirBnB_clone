#!/usr/bin/python3
'''
serialized and deserialized instances to a json file
'''
import json
from models.base_model import BaseModel


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
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            json.dump(my_dict, write_file)

    def reload(self):
        '''
        if __path file exits the deserialize the json file
        If not then do nothing
        '''
        new_dict = {}
        try:
            with open(self.__file_path, "r", encoding="utf-8") as read_file:
                new_dict = json.load(read_file)
            
            for key, value in new_dict.items():
                class_name = key.split(".")[0]
                class_type = globals().get(class_name)
                if class_type is not None:
                    self.new(class_type(**value))
                    #FileStorage.__objects[key] = BaseModel(**value)
                    #self.new(eval(key.split(".")[0])(**value))
        except IOError:
            pass
