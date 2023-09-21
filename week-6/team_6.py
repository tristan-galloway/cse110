"""

group: unathletic avengers
teacher: brother keers
file: team_6
goal: work as a team to write a program for a fictitious amusement park ride

"""


# The basic rules are as follows:
# 1. No one under 36 inches may ever ride, either by themselves or with another rider.
# 2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# 3. If there are two riders and one of them is at least 18 years old, they may ride together.

# default statements
can_ride = False

# CORE REQUIREMENTS
# 1.1 Prompt the user for the age and height of the first person.
age1 = int(input("What is the first riders age? "))
height1 = int(input("What is the height of the first rider in inches? "))
# Stretch 2, check if they have a golden ticket, if they do treat them as 18 years old
check_passport = input("Do you have a golden ticket (yes/no)? ").lower()
if check_passport == "yes":
    age1 = 18
second_rider = input("is there a second rider (yes/no)? ").lower()

# 1.2 Then, ask whether there is a second rider, and if so, ask for their age and height.
if second_rider == "yes":
    age2 = int(input("What is the first riders age? "))
    height2 = int(input("What is the height of the first rider in inches? "))
    # Stretch 2, check if they have a golden ticket, if they do treat them as 18 years old
    check_passport = input("Do you have a golden ticket (yes/no)? ").lower()
    if check_passport == "yes":
        age2 = 18

if height1 >= 36 and height2 >= 36:
    if age1 >= 18 or age2 >= 18:
        can_ride = True
    # Stretch Challenge 1. If both riders are under 18 but older than 12 and at least 52 inches, they can ride.
    elif (age1 >= 16 or age2 >= 16) and (age1 >= 14 and age2 >= 14):
        can_ride = True
    elif age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
        can_ride = True

# 2. Handle the case of a single rider.
else:
    if age1 >= 18 and height1 >= 62:
        can_ride = True
    # elif age1 >= 12 and golden_passport:
    #     can_ride = True

# 3. Finish implementing the basic rules.
if can_ride:
    print("\nWelcome to the ride. Please be safe and have fun!")
else:
    print("\nSorry, you may not ride.")
