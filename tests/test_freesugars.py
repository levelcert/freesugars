from __future__ import absolute_import, print_function
import unittest
from freesugars import free_sugars
from freesugars.__main__ import main

class TestFreeSugars(unittest.TestCase):

    def test_no_ingredients(self):
        self.assertEqual(0, free_sugars(ingredients={}, kilojoules=0))
        self.assertEqual(0, free_sugars(ingredients={}, kilojoules=100))

    def test_main(self):
        self.assertEqual(0, main([]))

