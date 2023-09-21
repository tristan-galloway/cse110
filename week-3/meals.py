"""

student: tristan galloway
teacher: brother keers
file: meals.py
assignment: 03 Prove Milestone - Meal Price Calculator
Goal: 

Compute the price of a meal as follows by asking for 
the price of child and adult meals, the number of each, 
and then the sales tax rate. Use these values to determine
the total price of the meal. Then, ask for the payment amount
and compute the amount of change to give back to the customer.

"""
import math

import colorama
from colorama import Fore

# Example of how to use colorama
#print(Fore.RED + 'This text is red in color')

# asks user for the cost of the meals for children and adults, then asks for the quantity and sales tax for their state
c_cost = float(input("What is the price of a childs meal? "))
a_cost = float(input("What is the price of a adults meal? "))
children = int(input("How many children are going to be eating? "))
adults = int(input("How many adults are going to be eating? "))
tax = float(input("What is sales tax rate? "))
tax = tax/100
tip = float(input("Percentage of tip (enter 0 to not tip): "))

# calculates the subtotal, tax fee, and combimes them to make a total
subtotal = float(f"{c_cost * children + a_cost * adults}")
tip = round((tip/100) * subtotal, 2)
tax_add = round(float(f"{subtotal * tax}"), 2)
total = round(float(subtotal + tax_add + tip), 2)

# Creating a multi line comment to print later returning to the user a summary of their purchase
fees = f"""
Subtotal: ${subtotal}
Tax: ${tax_add}
Tip: ${tip}
total: ${total}
"""

# prints the subtotal to the terminal
print(fees)

# ask for how much the user is paying with and returns the change amount
payment = float(input("What is the payment ammount? "))

# return the change they need to be given, if they didn't pay enough return the quantity still owed
change = round(float(payment - total), 2)

# if the payment given is less than the total, ask for more funds until the cost is paid
if change >= 0:
    print(Fore.GREEN + "\nTransaction Successfull!" + Fore.RESET)
    print(f"Change: ${change}")
else:
    while change <= 0:
        change = abs(change)
        print(Fore.RED + "\nInsufficiant funds" + Fore.RESET)
        print(f"Remaining Balance: ${change}")
        payment = float(input("What is the payment ammount? "))
        change = round(payment - change, 2)
    else:
        print(Fore.GREEN + "\nTransaction Successfull!" + Fore.RESET)
        print(f"Change: ${change}")