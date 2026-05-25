"""
Rock Paper Scissors Game
========================
A 1-player game where the user plays against the computer.

Rules:
- User chooses Rock, Paper, or Scissors
- Computer randomly picks one of the three
- Winner is decided by:
    * Rock beats Scissors
    * Scissors beats Paper
    * Paper beats Rock
- If both pick the same → It's a Draw
- Invalid input → Show error message

Modules needed: random
Key concepts:
- random module for computer pick
- if/elif/else for win condition logic
"""

import random

rock     = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper    = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissors]

user_choice = int(input("Please select 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice > 2 or user_choice < 0:
    print("You selected invalid number. Please restart the game and choose any of 0, 1, 2")
    exit()
else:    
    print(f"You selected: \n{images[user_choice]}")

computer_choice = random.randint(0,2)
print(f"Computer selected: \n{images[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw.")

elif user_choice == 0:
    if computer_choice == 1:
        print(f"Computer won: \n{images[computer_choice]}")
    elif computer_choice == 2:
        print(f"User won: \n{images[user_choice]}")

elif user_choice == 1:
    if computer_choice == 0:
        print(f"User won: \n{images[user_choice]}")
    elif computer_choice == 2:
        print(f"Computer won: \n{images[computer_choice]}")

elif user_choice == 2:
    if computer_choice == 0:
        print(f"Computer won: \n{images[computer_choice]}")
    elif computer_choice == 1:
        print(f"User won: \n{images[user_choice]}")
