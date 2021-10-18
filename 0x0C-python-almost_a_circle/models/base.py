#!/usr/bin/python3

import json
import os.path
import csv

"""
This module represents the base class for all 
subsequent classes in this package
"""

class Base:
    """
    This class represents the base for subsequent classes
    in this project

    Attributes:
     __nb_objects: this represents the unique object id

    >>> b1 = Base()
    >>> print(b1.id)
    1
    >>> b2 = Base()
    >>> print(b2.id)
    2
    >>> b3 = Base()
    >>> print(b3.id)
    3
    >>> b4 = Base(12)
    >>> print(b4.id)
    12
    >>> b5 = Base()
    >>> print(b5.id)
    4
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is called when a new instance of Base is created
            Args:
                id : is used to manage attributes and aboid creating same code
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_objects():
        """Resets number of objects for testing"""
        Base.__nb_objects = 0


    @staticmethod
    def to_json_string(list_dictionaries):
        if(list_dictionaries is None or len(list_dictionaries)== 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_cls = []
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as fp:
            if list_objs is not None:
                [list_cls.append(i.to_dictionary()) for i in list_objs]
            fp.write(cls.to_json_string(list_cls))

    @staticmethod
    def from_json_string(json_string):
        if json_string == None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            n = cls(1,1)
            n.update(**dictionary)
            return n
        elif cls.__name__ == 'Square':
            n = cls(1)
            n.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + '.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding= 'utf-8') as fp:
                ls_str_instance = Base.from_json_string(fp.read())
                ls_rl_instances = []
                [ls_rl_instances.append(cls.create(**i)) for i in ls_str_instance]
                return ls_rl_instances
        else:
            return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = cls.__name__ + '.csv'
        field_names = ['id','width', 'height', 'x', 'y'] if file_name == 'Rectangle.csv' else ['id','size', 'x', 'y']
        with open(file_name, 'w', encoding= 'utf-8') as fp:
            csv_w = csv.DictWriter(fp, fieldnames=field_names)
            csv_w.writeheader()
            [csv_w.writerow(i.to_dictionary()) for i in list_objs if list_objs is not None]
    
    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + '.csv'
        list_objs = []
        with open(file_name, 'r') as fp:
            csv_r = csv.DictReader(fp)
            for i in csv_r:
                for k, v in i:
                    i[k] = int(v)
                list_objs.append(cls.create(**i))