import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand: list) -> None:
    card = random.choice(CARDS)
    hand.append(validate_ace(hand) if card == 11 else card)


def validate_ace(hand: list) -> int:
    return 1 if sum(hand) + 11 > 21 else 11


def calculate_score(hand: list) -> int:
    return sum(hand)


def display_state(my_cards, computer_cards, final=False):
    if final:
        print(f"\t Your final hand: {my_cards}, final score: {calculate_score(my_cards)}")
        print(f"\t Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    else:
        print(f"\t Your cards: {my_cards}, current score: {calculate_score(my_cards)}")
        print(f"\t Computer's first card: {computer_cards[0]}")


def check_winner(my_score, computer_score):
    if computer_score > 21:
        print("Opponent went over. You win! 🎉")
    elif my_score > computer_score:
        print("You win! 🎉")
    elif my_score == computer_score:
        print("It's a draw!")
    else:
        print("Computer wins. 💀")


def play_round():
    my_cards = []
    computer_cards = []

    # Initial deal — 2 cards each
    deal_card(my_cards)
    deal_card(my_cards)
    deal_card(computer_cards)
    deal_card(computer_cards)  # dealer gets 2 cards, second stays hidden

    display_state(my_cards, computer_cards)

    # Blackjack check — both hands revealed immediately, no extra draws
    if calculate_score(my_cards) == 21:
        display_state(my_cards, computer_cards, final=True)
        if calculate_score(computer_cards) == 21:
            print("Both have Blackjack! It's a draw! 🤝")
        else:
            print("Blackjack! You win! 🎉")
        return

    # Player's turn
    while True:
        user_choice = input("Type 'y' to pick another card, 'n' to pass: ").lower()
        if user_choice == 'y':
            deal_card(my_cards)
            if calculate_score(my_cards) > 21:
                display_state(my_cards, computer_cards, final=True)
                print("You went over. You lose. 💀")
                return
            display_state(my_cards, computer_cards)
        else:
            break

    # Computer's turn — draws until 17
    while calculate_score(computer_cards) < 17:
        deal_card(computer_cards)

    display_state(my_cards, computer_cards, final=True)
    check_winner(calculate_score(my_cards), calculate_score(computer_cards))


# Main loop
while True:
    user_input = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_input != 'y':
        print("Thanks for playing. Bye! 👋")
        break
    print("\n" * 20)
    print(logo)
    play_round()