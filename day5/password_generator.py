"""
Password Generator
-----------------
Generates a random secure password based on user input.

Rules:
- Ask user how many letters they want
- Ask user how many symbols they want
- Ask user how many numbers they want
- Randomly pick from each category
- Shuffle the final list so it's not predictable
- Print the final password as a string

Modules needed: random
Key concepts:
- for loop to pick random characters
- random.choice() from character lists
- random.shuffle() to mix the password
- ''.join() to convert list → string

Character sets:
- Letters: ['a','b','c' ... 'z', 'A'...'Z']
- Numbers: ['0','1','2' ... '9']
- Symbols: ['!','@','#','$','%','^','&','*']
"""

import random

print("Welcome to the Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

password = []

for i in range(letters_count):
    password.append(random.choice(letters))

for i in range(symbols_count):
    password.append(random.choice(symbols))

for i in range(numbers_count):
    password.append(str(random.randint(0,9)))

random.shuffle(password)

final_password = ''.join(password)

print(f"Here is the recommended password: {final_password}")






