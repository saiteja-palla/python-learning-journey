"""
Life in Weeks
-------------
Calculates how many weeks are left in a person's life.

Rules:
- Assume life expectancy = 90 years
- weeks_left = (90 - age) * 52
- Print the result

Key concepts:
- Function with single parameter
- Basic arithmetic
- f-string output
"""

def life_in_weeks(age):
    weeks_in_a_year = 52
    years_left = 90 - age
    weeks_left = years_left * weeks_in_a_year
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)