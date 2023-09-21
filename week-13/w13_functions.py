"""

student: tristan galloway
teacher: brother keers
file: w13_functions.py
assignment: Demonstration of the use of functions

"""

# Just prints the users original string
def display_regular(message):
    print(message)

# Makes user input Uppercase
def display_uppercase(msg):
    up = msg.upper()
    print(up)

# Makes user input lowercase
def display_lowercase(m):
    low = m.lower()
    print(low)

    
# Ask the user for a string to modify using fucntions
user_txt = input("What text would you like to modify? ")

# Call the functions to print
display_regular(user_txt)
display_uppercase(user_txt)
display_lowercase(user_txt)