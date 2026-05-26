"""
FizzBuzz
--------
Classic programming challenge using for loop and modulo operator.

Rules:
- Loop through numbers 1 to 100
- If divisible by both 3 and 5 → print "FizzBuzz"
- If divisible by 3 only        → print "Fizz"
- If divisible by 5 only        → print "Buzz"
- Otherwise                     → print the number

Key concepts:
- for loop to iterate 1 to 100
- range(1, 101) to generate numbers
- modulo operator % to check divisibility
- if/elif/else for condition chaining
"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)