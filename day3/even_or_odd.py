"""
Even or Odd Number Exercise
---------------------------

Find whether the user input value is even or odd using modulo operator.

Test case:
    input : 34
    output : Even
"""

number = int(input("Please enter an integer number to find whether its Even or Odd: "))

if number % 2 == 0:
    print(f"The number {number} is an even number")
else:
    print(f"The number {number} is an odd number")