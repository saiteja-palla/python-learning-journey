"""
Leap Year Checker
----------------
Determines whether a given year is a leap year.

Rules:
- year % 4 == 0   → potential leap year
- year % 100 == 0 → not a leap year (century year)
- year % 400 == 0 → is a leap year (exception to century rule)

Examples:
    is_leap_year(2020) → True   (div by 4, not 100)
    is_leap_year(1900) → False  (div by 100, not 400)
    is_leap_year(2000) → True   (div by 400)
    is_leap_year(2023) → False  (not div by 4)
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False   
        else:
            return True
    return False

print(is_leap_year(2020))   
print(is_leap_year(1900))   
print(is_leap_year(2000))   