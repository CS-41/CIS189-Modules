"""
Program: camper_age_input.py
Author: Elizabeth Allen
Last date modified: 06/03/2020

The purpose of this program is to convert a camper's age from years to months.
The input can be any integer representing an age in years.
The output will be two statements, one re-stating the camper's age in years and a second
will show the camper's age in months.
"""
import unittest

age_in_years = input("Enter camper age in years: ")  # Input camper age.
YEARS_TO_MONTHS = 12  # Constant representing months.
a = int(age_in_years)  # Converted to integer for math reasons.
b = YEARS_TO_MONTHS


def convert_to_months(a, b):
    return a * b


age_in_months = convert_to_months(a, b)

print(f"Your camper's age in years is: {age_in_years}.")
print(f"Your camper's age in months is: {age_in_months}.")

if __name__ == '__main__':
    unittest.main()

# This is the finished camper_age_input.
