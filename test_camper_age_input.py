"""
Program: test_camper_age_input.py
Author: Elizabeth Allen
Last date modified: 06/03/2020

This is a program specific to testing the program camper_age_input.py.
The input is to test the function convert_to_months with the values 3 and 12, compared to the expected output, 36.
The ouput will be either ignoble failure or glorious success.

NOTE: I wasn't able to get the program to import the camper.age.input file until it corrected my syntax from:
"from camper_age_input import convert_to_months" to "from main.camper_age_input import convert_to_months"

This was literally on the 20th try to get this to work. I don't know why PyCharm corrected me then as opposed
to the first time I made this error. I mention this because this syntax does NOT appear in the web resources I tried,
nor in the assignment instructions. Did I miss something?

"""


import unittest
from main.camper_age_input import convert_to_months


class FunctionTestCase(unittest.TestCase):
    def test_years_to_months(self):
        months = convert_to_months(3, 12)
        self.assertEqual(months, 36)


if __name__ == '__main__':
    unittest.main()
