#!/usr/bin/python3
"""
This is 'review' module.
Functions and Classes:
    class User(BaseModel):
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """representing a review"""

    place_id = ""
    user_id = ""
    text = ""
