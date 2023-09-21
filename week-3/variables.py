import math

"""

student: tristan galloway
teacher: brother keers
assignment: 03 prepare: checkpoint "Numeric Data Types"
Goal:
1. Prompt the user for their age. 
    Convert it to a number
        add one to it 
            and tell them how old they will be on their next birthday.

2. Prompt the user for the number of egg cartons they have. 
    Assume each carton holds 12 eggs 
        multiply their number by 12
             and display the total number of eggs

3. Prompt the user for a number of cookies and a number of people
    Then, divide the number of cookies by the number of people to determine how many cookies each person gets.


"""
# ask the user for their age, then tell them how old they will be on their next birthday
age = int(input("How old are you? "))
print(f"On your birthday, you will turn {age + 1} years old!")

# ask the user for how many cartons of eggs they have, then return how many individual eggs they have
eggs = int(input(f"\nHow many egg cartons do you have in your home? "))
print(f"You have a total of {eggs * 12} eggs.")

# asks how many cookies they have and how many people they will be split by then returns the number to the user
cookies = int(input(f"\nHow many cookies do you have? "))
people = int(input(f"How many people are they being shared with? "))
share = float(cookies / people)

# changes the response based on whether or not the amount of cookies being shared is plural or not
if share > 1:
    print(f"You will have enough to give each person {share} cookies!")
else:
    print(f"You will have enough to give each person {share} cookie!")