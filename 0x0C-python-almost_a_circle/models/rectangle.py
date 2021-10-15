from models.base import Base

class Rectangle (Base):
    """This is a rectangle class

    Attributes:
    id: id of object
    width: width of the rectangle
    height: height of the rectangle
    x: x coordinate of rectangle
    y: y coordinate of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width =  width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """
        Get value of width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Sets the value of width
        """
        self.__width = self.validate('width', value)
    
    
    @property
    def height(self):
        """
        Get Value of __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of private instance variable __height
        """
        self.__height = self.validate('height', value)
    
    @property
    def x(self):
        """
        Get value of __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets Value of __x
        """
        self.__x = self.validate('x', value)
    
    @property
    def y(self):
        """
        Gets Value of private instance variable __y
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        sets the value of __y
        """
        self.__y = self.validate('y', value)

    def validate(self, prop, val):
        """
        This is a helper class for validating inputs to private instance attributes
        """
        
        if(type(val) is not int):
            raise TypeError('{} must be an integer'.format(prop))
        if(val < 0):
            if (prop in ['x', 'y']):
                raise ValueError('{} must be >= 0'.format(prop))
            else:
                raise ValueError('{} must be > 0'.format(prop))
        return val
    

    def area(self):
        return self.width * self.height
    
    def display(self):
        """
        This prints the rectangle to the 
        Terminal
        """
        [print('#' * self.width) for i in range(self.height)]
