"""
Coin Flip Simulator
===================
Simulates a random coin toss and tells the user the result.

Rules:
- Randomly pick either 'Heads' or 'Tails'
- Print the result to the user

Modules needed: random
"""

import random

#Method 01
random_value = random.randint(0,1)
if random_value == 0:
    print ("Heads")
else:
    print("Tails")

#Method 02
possible_outcomes = ["Heads", "Tails"]
print(random.choice(possible_outcomes))