import unittest
from unittest.case import TestCase
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib

class TestRectangle (TestCase):
    
    def test_ValueError(self):
        with self.assertRaises(ValueError):
             rect = Rectangle(12, 10, -1, 1)
        with self.assertRaises(ValueError):
             rect = Rectangle(-12, 10, 1, 1)
        with self.assertRaises(ValueError):
             rect = Rectangle(12, -10, 1, 1)
        with self.assertRaises(ValueError):
             rect = Rectangle(12, 10, 1, -1)

    "#TEST  TYPE ERRORS"
    def test_TypeError(self):
        with self.assertRaises(TypeError):
             rect = Rectangle(12, 10, False, 1)
        with self.assertRaises(TypeError):
             rect = Rectangle(12, 10, 1, "3")
        with self.assertRaises(TypeError):
             rect = Rectangle(12, False, 1, 1)
        with self.assertRaises(TypeError):
             rect = Rectangle("12", 10, 1, 1)

    def test_Area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display__method(self):
        """This function tests the display function"""
        r1 = Rectangle(3, 3, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "###\n###\n###\n")

    def test_str(self):
         r1 = Rectangle(4, 6, 2, 1, 12)
         self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')
         r2 = Rectangle(5, 5, 1)
         self.assertEqual(r2.__str__(), f'[Rectangle] ({r2.id}) 1/0 - 5/5')