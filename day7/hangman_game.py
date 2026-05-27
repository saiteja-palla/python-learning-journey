"""
Hangman Game
------------
Classic word guessing game — guess the word before you run out of lives.

Rules:
- Random word selected from word_list using random.choice()
- Placeholder built as list of '-' matching word length
- Player guesses one letter at a time
- Correct guess → placeholder updated at matching index
- Wrong guess → lives reduced by 1
- Win condition  → '-' not in placeholder
- Lose condition → lives == 0
- 6 lives total, each wrong guess shows next hangman stage

Modules needed: random
Key concepts:
- while loop with break for game flow
- for loop + range() to check each character
- list() to make placeholder mutable
- ''.join() to display placeholder as string
- .lower() for case-insensitive comparison
- in operator to check win condition
- stages[] list indexed by lives for ASCII art
"""

import random 

word_list = [
    "ardvark", "baboon", "camel", "diamond", "elephant",
    "falcon", "guitar", "horizon", "island", "jungle",
    "kangaroo", "lemon", "mango", "notebook", "orange",
    "python", "quantum", "rocket", "sunset", "tiger",
    "umbrella", "violet", "walrus", "xenon", "yellow", "zebra"
]

stages = [
    # Stage 6 - head, body, both arms, both legs
    """
    -----
    |   |
    O   |
   /|\  |
   / \  |
        |
---------
    """,
    # Stage 5 - head, body, both arms, one leg
    """
    -----
    |   |
    O   |
   /|\  |
   /    |
        |
---------
    """,
    # Stage 4 - head, body, both arms
    """
    -----
    |   |
    O   |
   /|\  |
        |
        |
---------
    """,
    # Stage 3 - head, body, one arm
    """
    -----
    |   |
    O   |
   /|   |
        |
        |
---------
    """,
    # Stage 2 - head and body
    """
    -----
    |   |
    O   |
    |   |
        |
        |
---------
    """,
    # Stage 1 - head only
    """
    -----
    |   |
    O   |
        |
        |
        |
---------
    """,
    # Stage 0 - empty gallows
    """
    -----
    |   |
        |
        |
        |
        |
---------
    """,
]

guessed_letters = []
random_word_from_word_list = random.choice(word_list)

placeholder = '-'*len(random_word_from_word_list)
print(placeholder)

placeholder = list(placeholder)

lives = 6

while lives > 0:

    is_match = False
    char_choosen = input('Guess a character: ')

    if char_choosen in guessed_letters:
        print(f"Already guessed: '{char_choosen}'!")
        continue

    guessed_letters.append(char_choosen)

    for i in range(len(random_word_from_word_list)):

        if random_word_from_word_list[i].lower() == char_choosen.lower():
            placeholder[i] = char_choosen
            is_match = True

    if is_match:

        print(''.join(placeholder))
        print(stages[lives])

        if '-' not in placeholder:
            print("You Won :)")
            break

    if not is_match:

        lives -= 1

        if lives == 0:
            print(''.join(placeholder))
            print("You Lost")
            print(stages[lives])
            break

        print(''.join(placeholder))
        print(stages[lives])


        

        

    