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
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
         r1 = Rectangle(4, 6, 2, 1, 12)
         self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')
         r2 = Rectangle(5, 5, 1)
         self.assertEqual(r2.__str__(), f'[Rectangle] ({r2.id}) 1/0 - 5/5')
     
     
    def test_updatekwargswidth(self):
     """This function tests updating width with kwargs"""
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(width=1)
     self.assertEqual(r1.width, 1)

    def test_updatekwargsheight(self):
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(height=2)
     self.assertEqual(r1.height, 2)

    def test_updatekwargsx(self):
     """This function tests updating x with kwargs"""
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(x=3)
     self.assertEqual(r1.x, 3)

    def test_updatekwargsy(self):
     """This function tests updating y with kwargs"""
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(y=4)
     self.assertEqual(r1.y, 4)

    def test_updatekwargsid(self):
     """This function tests updating id with kwargs"""
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(id=5)
     self.assertEqual(r1.id, 5)

    def test_updatekwargsall(self):
     """This function tests updating all attrs with kwargs"""
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(width=5, height=5, x=5, y=5, id=5)
     self.assertEqual(r1.width, 5)
     self.assertEqual(r1.height, 5)
     self.assertEqual(r1.x, 5)
     self.assertEqual(r1.y, 5)
     self.assertEqual(r1.id, 5)

    def test_kwargsskipped(self):
     """This function tests updating args with kwargs"""
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(1, 2, 3, 4, 5, id=10)
     self.assertEqual(r1.id, 1)

    def test_badkeyignored(self):
     r1 = Rectangle(10, 10, 10, 10, 10)
     r1.update(1, 2, 3, 4, 5, foo=20)
     self.assertEqual(r1.id, 1)
     self.assertEqual(r1.width, 2)
     self.assertEqual(r1.height, 3)
     self.assertEqual(r1.x, 4)
     self.assertEqual(r1.y, 5)
