#!/usr/bin/python3

'''
This is a base model that defines all common attributes and
methods of other classes
'''

from datetime import datetime


class BaseModel:
    '''
    represents the base model class
    '''

    def __init__(self, *args, **kwargs):
        '''
        constructor
        '''

        if not kwargs:
            self.creted_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%M-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%M-%dT%H:%M:%S.%f')
            
    def save(self):
        '''
        update public update at current time instance
        '''
        self.updated_at = datetime.now()
        storage,save
