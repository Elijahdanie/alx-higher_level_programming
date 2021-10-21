import unittest
from unittest.case import TestCase
from models.base import Base

"""
This module test the base class

"""

class TestBase (TestCase):

    def test_Instances(self):
        base = Base()
        another = Base()
        self.assertEqual(another.id, 2)
        finalone = Base(5)
        self.assertEqual(finalone.id, 5)