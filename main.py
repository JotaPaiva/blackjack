import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    user_cards = []
    computer_cards = []
    game_over = False
    computer_score = -1
    user_score = -1

    print(art.logo)

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour hand: {user_cards}")
        print(f"Your score: {user_score}")

        print(f"\nComputer's first card: {computer_cards[0]}")
        
        if user_score > 21 or user_score == 0 or computer_score == 0:
            print("\n-------------------------------------------")
            game_over = True
        else:
            print("\n-------------------------------------------")
            user_should_deal = input("\nDo you want another card? Type 'y' or 'n': ").lower()

            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}")
    print(f"Your final score: {user_score}")

    print(f"\nComputer's final hand: {computer_cards}")
    print(f"Computer's final score: {computer_score}")

    print(f"\n{compare(user_score, computer_score)}")

    print("\n-------------------------------------------")

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game()
