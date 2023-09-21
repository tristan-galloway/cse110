"""

student: tristan galloway
teacher: brother keers
file: wordle.py
assignment: 

"""
import random

# Welcome the user
print("Welcome to the Walmart Wordle!")
play_game = "yes"
points = 100

# Make it so they can continue to play after the first word
while play_game == "yes":

    # week 7, 01. Have a secret word stored in the program. (making it my own by having an list of words that are randomly selected)
    word_list = ["monitor", "program", "application", "keyboard", "javascript", "gaming", "network"]
    secret_word = word_list[random.randint(0, 6)]
    hint        = ""
    guess       = ""
    guesses     = 0

    # weeek 8, 03. Use a loop to generate the initial hint.
    for _ in secret_word:
        hint += "_ "

    # week 7, 03. Continue looping as long as that guess is not correct.
    while guess != secret_word:

        print(f"\nYour hint is: {hint}")

        # week 7, 02. Prompt the user for a guess.
        guess = input("What is your guess? ").lower()

        # week 7, 03. Calculate the number of guesses and display it at the end.
        guesses += 1

        # week 8, 02. Add a check to verify that the length of the guess is the same as the length of the secret word. If it is not, display a message. If they are the same, then proceed to give the hint. 
        if len(guess) != len(secret_word):
            guess = input(f"Please enter a guess that is {len(secret_word)} characters long: ").lower()
            continue

        # Reset hint if it has been used already so the pogram can build it off of a new guess
        hint = ""

        # week 8, 04. Make sure to account for the following in your hints:
        for i, letter in enumerate(guess):
            # if the letter is correct and in the correct place make it uppercase
            if letter == secret_word[i]:
                hint += letter.upper()
            # if the letter is in the word but not the right place, make it lowercase
            elif letter in secret_word:
                hint += letter.lower()
            # if the letter is not in the word, put an underscore
            else:
                hint += "_"

        points += -guesses * 5

    print(f"\nCongratulations! You guessed it! It took you {guesses} guesses.")
    print(f"You've earned {points} points!")

    play_game = input("\nWould you like to play again (yes/no)? ").lower()

print("\nThank you for playing Walmart Wordle!")
