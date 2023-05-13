#!/usr/bin/python3
"""Defining a class called BaseModel"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Defines all common attributes/method for other classes"""

    def __init__(self, *args, **kwargs):
        """"Initializes the BaseModel class with 3 public
        instance attributes
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance attributes"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at instance attribute with current datetime"""
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys and values of __dict__"""

        dict_dup = self.__dict__.copy()
        dict_dup['__class__'] = self.__class__.__name__
        dict_dup['created_at'] = dict_dup['created_at'].isoformat()
        dict_dup['updated_at'] = dict_dup['updated_at'].isoformat()
        return dict_dup
