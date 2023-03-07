import random
from art import logo 
from art import vs
from game_data import data

#constants
print(logo)
random_list = random.sample(data, len(data))
keep_going = True
points = 0
while keep_going:
    first_person = random_list[0]
    second_person = random_list[1]
    first_name = first_person["name"]
    second_name = second_person["name"]
    first_followers = int(first_person["follower_count"])
    second_followers = int(second_person["follower_count"])
    first_description = first_person["description"]
    second_description = second_person["description"]
    first_country = first_person["country"]
    second_country = second_person["country"]
    
    
    print(f"Compare A: {first_name}, a {first_description}, from {first_country}.")
    print(vs)
    print(f"Against B: {second_name}, a {second_description}, from {second_country}.")
    winner = max(first_followers, second_followers)
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == "A":
        if winner == first_followers:
            points += 1
            print(f"You're right! Current score: {points}")
            random_list.pop(0) 
        else:
            print(f"Sorry, that's wrong. Final score: {points}")
            keep_going = False
    elif guess == "B":
        if winner == second_followers:
            points += 1
            print(f"You're right! Current score: {points}")
            random_list.pop(0)
        else:
            print(f"Sorry, that's wrong. Final score: {points}")
            keep_going = False
    else:
        keep_going = False
        print("Input not recognized, please input 'A' or 'B'.")
        