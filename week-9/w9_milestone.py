"""

student: tristan galloway
teacher: brother keers
file: w9_milestone.py
objective: For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

"""

import math

# Week 9 01. Have menu system that repeats until the user chooses quit.

menu = ["Add item", "View cart", "Remove Item", "Compute total", "Quit"]
shopping_cart = []

while True:

    # Display the menu and ask the user what action they would like to do
    for i, menu_item in enumerate(menu):
        print(f"[{i + 1}] {menu_item}")

    action = input("Please enter an action: ").strip()

    # Ask user what Item they would like to add to the shopping cart and append it
    if action == "1":
        item = input("What item would you like to add? ")
        shopping_cart.append(item)

    # Display the Items that have been added to the shopping cart so far
    elif action == "2":
        for i, j in enumerate(shopping_cart):
            print(f"{i + 1}. {j}")
            print("")

    # Ask the user what item they would like to remove and complete the task
    elif action == "3":
        remove = input("what item would you like to remove? ")
        if remove in shopping_cart:
            # figure out how to del the input out of shopping list
            del shopping_cart[str(remove)]
        else:
            print("Make sure the to type the item you'd like to remove the exact same way as when you added it.")
            continue

    elif action == "4":
        ...

    elif action == "5":
        break

    else:
        print("Please choose a valid option.")

print("Thank you! Goodbye.")

# try:
#     ...
# except:
#     ...