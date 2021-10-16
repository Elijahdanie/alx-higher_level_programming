from logging import setLogRecordFactory
from typing import Sized
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)
    
    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
    
    @property
    def size(self):
        return self.height
    
    @size.setter
    def size(self, value):
        self.height = value
        self.width = value
    
    def update(self, *args, **kwargs):
        prop = ['id','size', 'x', 'y']
        len_args = len(args)
        if len_args > 0:
            [setattr(self, prop[i], args[i]) for i in range(len_args)]
        else:
            [setattr(self, k, v) for k, v in kwargs.items() if k in prop]

    def to_dictionary(self):
        prop = ['id','size', 'x', 'y']
        dict_ ={}
        for i in prop:
            dict_[i] = getattr(self, i)
        return dict_