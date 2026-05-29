"""
Calculator
----------
A command-line calculator that supports chaining operations.

Rules:
- User enters first number
- Choose from +, -, *, / operations
- Enter second number → result displayed
- Option to continue with result as new first number
- Repeat until user exits with 'n'
- Division by zero handled gracefully
"""

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = float(input("Enter the first number: "))
is_repeat = True

while is_repeat:
    for key in operations:
        print(key)
    input1 = input("Enter the operation: ")
    num2 = float(input("Enter the second number: "))

    if input1 == '/' and num2 == 0:
        print("Cannot divide by zero!")
        continue

    result = operations[input1](num1, num2)
    print(f"Result: {result}")

    repeat = input(f"Press 'y' to continue with {result}, or 'n' to exit: ").lower()
    if repeat == 'y':
        num1 = result   
    else:
        is_repeat = False