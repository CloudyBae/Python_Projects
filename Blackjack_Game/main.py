import random
from art import logo
import os

def deal_card():
    """picks a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
       
def calculate_score(cards):
        """Adds up the sum of all the cards in the list"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11).append(1)
        return sum(cards)

def compare(user_score, computer_score):
    """Compares the user & computer scores to each other"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer hit blackjack! You lose."
    elif user_score == 0:
        return "You hit blackjack! You win."
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Computer went over, you win."
    elif user_score > computer_score:
        return "Your hand is higher than computer, you win."
    else:
        return "Your hand is lower than computer, you lose."
    
def play_game():
    """Blackjack game"""
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Do you want to draw another card? Say 'yes' or 'no': ")
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    os.system("cls")
    play_game()
        