#!/usr/bin/python3
"""
inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for representing reviews with public attributes.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a Review object.
        """
        super().__init__(*args, **kwargs)

