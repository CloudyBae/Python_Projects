import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices = [rock, paper, scissors]
if user > 2:
    print("Sorry, you can only choose between 0, 1 or 2.")
else: 
    print(choices[user])

    print("Computer chose:")

    computer_choice = random.randint(0, 2)
    print(choices[computer_choice])

    if user == 0 and computer_choice == 2:
        print("You win!")
    elif user == 2 and computer_choice == 1:
        print("You win!")
    elif user == 1 and computer_choice == 0:
        print("You win!")
    elif user == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")
    

