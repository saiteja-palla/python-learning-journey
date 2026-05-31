import random

EASY_LEVEL = 10
HARD_LEVEL = 5

logo = r""" _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ """

def check_answer(guess: int, computer_pick: int, attempts: int) -> bool:
    if guess < computer_pick:
        print("Too low")
        print("Guess again")
        print(f"You have {attempts} remainign to guess the game.")
        return False
    elif guess > computer_pick:
        print("Too high")
        print("Guess again")
        print(f"You have {attempts} remainign to guess the game.")
        return False
    else:
        print(f"You got it. The answer was {computer_pick}.")
        return True

def play_game(computer_pick: int) -> None:
    difficulty_level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'hard':
        attempts = HARD_LEVEL
    else:
        attempts = EASY_LEVEL

    while attempts >= 1:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if check_answer(guess, computer_pick, attempts):
            break
        else:
            continue
    else:
        print("You lost the game")

print(logo)
print("Welcome to the Number Guesing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_pick = random.randint(1, 100)
play_game(computer_pick)
    