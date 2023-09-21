"""

group: unathletic avengers
teacher: brother keers
file: team_7
assigment: In the Guess My Number game the computer picks a magic number, and then the user tries to guess it. After each guess, the computer tells the user to guess "higher" or "lower" until they guess the magic number.

"""

import random


play_game = "yes"

# wrap this in a wile play_game is "yes" statement
while play_game == "yes":

    magic_number = random.randint(1, 100)
    print("The computer has chosen a magic number, your job is to guess it in as few attemps as possible.")
    guess = int(input("What is your guess? "))
    guess_count = 1

    while guess != magic_number:
        guess_count += 1

        # If the guess is higher then the magic number, let them know to guess lower
        if guess > magic_number:
            print("Lower")
            guess = int(input("What is your guess? "))

        # If the guess is lower then the magic number, let them know to guess higher
        elif guess < magic_number:
            print("Higher")
            guess = int(input("What is your guess? "))

    # Let the user know they guessed it correctly and how many attempts it took
    print(f"You guessed it! it took you {guess_count} attempts.")

    # Ask the user if they'd like to play again
    play_game = input("Would you like to play again (yes/no)? ")
else:
    print("\nThank you for playing!")