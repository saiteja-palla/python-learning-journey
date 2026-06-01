"""
A terminal-based game where the player guesses which celebrity or brand
has more Instagram followers. Score increases on every correct guess.
"""

from random import choice
from game_data import data
from art import logo, vs

guess_count = 0

def random_pick():
    return choice(data)

def call_out(person_a, person_b):
    print(f"Compare A: {person_a.get('name')}, a {person_a.get('description')}, from {person_a.get('country')}.")
    print(vs)
    print(f"Compare B: {person_b.get('name')}, a {person_b.get('description')}, from {person_b.get('country')}.")

def compare_followers(data1, data2):
    global guess_count
    if data1 > data2:
        guess_count += 1
        print("\n" * 20)
        print(logo)
        print(f"You are right! Current score: {guess_count}.")
        return True
    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {guess_count}.")
        return False

def play_game(seen_entries):
    print(logo)
    person_a = random_pick()
    seen_entries.append(person_a)
    while True:
        if len(seen_entries) >= len(data) - 1:
            print("You've seen everyone! Game over.")
            break
        person_b = random_pick()
        while person_b in seen_entries:
            person_b = random_pick()
        seen_entries.append(person_b)
        call_out(person_a, person_b)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        try:
            if user_choice == 'a':
                if compare_followers(person_a.get('follower_count'), person_b.get('follower_count')):
                    continue
                break
            elif user_choice == 'b':
                if compare_followers(person_b.get('follower_count'), person_a.get('follower_count')):
                    person_a = person_b
                    continue
                break
            else:
                raise ValueError
        except ValueError:
            print("Sorry, that's not a valid choice.")
            continue

seen_entries = []
play_game(seen_entries)
