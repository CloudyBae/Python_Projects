import os
import random
from art import logo

Turns_easy = 10
Turns_hard = 5

def compare(guess, number, turns):
    """checks guess against number & returns turns remaining"""
    if guess == number:
        correct = print(f"You got it! The answer was {number}.")
        return correct
    elif guess < number:
        print("Too low.")
        return turns - 1
    else:
        too_high = print("Too high.")
        return turns - 1

def set_difficulty():
    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return Turns_easy
    if difficulty == "hard":
        return Turns_hard
    
def game():    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(0, 100)
        
    turns = set_difficulty() 
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaning to guess the number.") 
        guess = int(input("Make a guess: "))
        turns = compare(guess, number, turns) 
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")

while input("Do you want to play the Number Guessing Game? Type 'yes' or 'no': ") == "yes":
    os.system("cls")
    game()