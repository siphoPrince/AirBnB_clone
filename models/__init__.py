#!/usr/bin/python3
""" __ini__ module"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel
storage = FileStorage()
storage.reload()
