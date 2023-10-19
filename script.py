import random


def calculate_score(cards):
    score = 0
    aces = 0

    for card in cards:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            aces += 1
        else:
            score += card

    for _ in range(aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    return score


def get_card():
    return random.choice(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])


def blackjack_game():
    player_cards = [get_card(), get_card()]
    player_total = 0

    computer_cards = [get_card(), get_card()]
    computer_total = 0

    print(
        f"Your cards are: {player_cards}\nComputer's first card is : {computer_cards[0]}")
    add_card = input(
        "Type 'y' to get another card, type 'n' to pass: ").lower()

    while add_card == 'y':
        player_cards.append(get_card())
        print(
            f"Your cards are: {player_cards}\nComputer's first card is : {computer_cards[0]}")
        player_total = calculate_score(player_cards)

        if player_total > 21:
            add_card = 'n'
        else:
            print(f"Your total is {player_total} do you want to continue?")
            add_card = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
    player_total = calculate_score(player_cards)
    computer_total = calculate_score(computer_cards)

    while computer_total < 15:
        computer_cards.append(get_card())
        computer_total = calculate_score(computer_cards)

    if player_total > computer_total and player_total < 22 and computer_total < 22 or player_total < 22 and computer_total > 21:
        print(
            f"You won! Your score is {player_total} and computer's is {computer_total}")
    elif player_total == computer_total and player_total < 22 and computer_total < 22:
        print(
            f"It's a draw! Both you and the computer had a total of {player_total}")
    else:
        print(
            f"You lost! Your score was {player_total} while computer's was {computer_total}")


playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while playing == 'y':
    blackjack_game()
    playing = input("Do you want to play again? Type 'y' or 'n': ")
