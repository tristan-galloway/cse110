"""

student: tristan galloway
teacher: brother keers
file: loops.py
Assignment: Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

"""

# Assignment 1
# Asking user for a positive number
pos_int = int(input("Please type a positive number: "))

# If they type a negative number let them know and ask for a positive number again.
while pos_int < 0:
    print("Sorry, that is a negative number. Please try again.")

    pos_int = int(input("Please type a positive number: "))

# Return the successful positive number to user
print(f"The number is: {pos_int}")


# Assignment 2
# Ask user for candy
candy_request = input("May I have a piece of candy? ").lower()

# If response is no, repeat until they say yes... annoy them
while candy_request != "yes":
    candy_request = input("May I have a piece of candy? ")

# Thank them for caving and letting me have candy
print("Thank you.")