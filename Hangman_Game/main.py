import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

#picks a random word from the imported word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Create blanks
letters_guessed = []
display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in letters_guessed:
        print(f"You have already guessed the letter {guess}, please choose a different letter.")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letters_guessed.append(guess)

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not a part of the word.")
        lives -= 1
        print(f"You have {lives} lives left.")
        letters_guessed.append(guess)
        if lives == 0:
            end_of_game = True
            print("You lose.")
    

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])