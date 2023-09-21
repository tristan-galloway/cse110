"""

student: tristan galloway
teacher: brother keers
file: if_else.py
goal: Practice the mechanics of if statements.

"""

# collect two numbers from the user to compare later on
int1 = int(input("Please give a whole number: "))
int2 = int(input("Please give another whole number: "))

# Identify if int1 2 is greater and return the response to the user.
if int1 > int2:
    print("\nThe first number is greater.")
else:
    print("The first number is not greater.")

# Identify if the ints are equal and return the response to the user.
if int1 == int2:
    print("The numbers are equal.")
else:
    print("The numbers are not eqaul.")

# Identify if int 2 is greater and return the response to the user.
if int2 > int1:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

#------------------------------------------------------------------------------
# Animal portion

# ask the user for their favorite animal
user_animal = input("\nWhat is your favorite animal? ").capitalize()

# compare our favorite animals to see if they are the same
if user_animal == "Panda":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")