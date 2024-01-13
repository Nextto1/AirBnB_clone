#!/usr/bin/python3
"""Module for User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """A class that represents a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
