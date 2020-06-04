"""
Program: test_functions.py
Author: Elizabeth Allen
Last date modified: 06/03/2020

The purpose of this program is to show the preliminary test file.
The input is 3.
The output will be an error, per the instructions.
"""


import unittest
from main.camper_age_input_prelim import convert_to_months

class FunctionTestCase(unittest.TestCase):
    def test_months(self):
         months = convert_to_months(3)
         self.assertEqual(3)


if __name__ == '__main__':
    unittest.main()
