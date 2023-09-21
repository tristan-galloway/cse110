"""

student: tristan galloway
teacher: brother keers
file: w10_milestone.py
objective: For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

"""
 
import math

# Create the global lists to build the main menu, shopping cart, and prices of the items added
menu = ["Add item", "View cart", "Remove Item", "Compute total", "Quit"]
shopping_cart = []
item_price = []

print("Welcome to jank amazon!")

# Week 9 01. Have menu system that repeats until the user chooses quit.
while True:

    # Each time the user completes an action, print the menu and ask what they would like to do.
    print("")
    for i, menu_item in enumerate(menu):
        print(f"[{i + 1}] {menu_item}")

    action = input("Please enter an action: ").strip()

    # Ask user what Item they would like to add to the shopping cart and append it as well as ask for the price and append it to the cost list
    if action == "1":
        item = input("What item would you like to add? ")
        price = float(input("How much does the item cost? "))
        shopping_cart.append(item)
        item_price.append(price)

    # Display the Items that have been added to the shopping cart
    elif action == "2":
        print("\nThe shopping cart contains these items:")
        for i in range(len(shopping_cart)):
            ind_item = shopping_cart[i]
            ind_price = item_price[i]

            print(f"{i + 1}. {ind_item:.<30} ${ind_price:,.2f}")

    # Ask the user what item they would like to remove and complete the task
    elif action == "3":
        remove = int(input("What number would you like to remove? "))

        # If the user enters a number that is too large, have them try again
        if remove - 1 > len(shopping_cart):
            print("Please enter a valid number from your shopping cart. ")
            continue

        else:
            new_item = input("What is the new item? ")
            new_price = float(input("What is the new price of the item? "))
            
            shopping_cart[remove - 1] = new_item
            item_price[remove - 1] = new_price

    # Build a running total of the cost of the items in the shopping cart and return it to the user
    elif action == "4":

        running_total = 0

        for i in range(len(item_price)):
            ind_price = item_price[i]
            running_total += ind_price

        print(f"The Subtotal for your cart is: ${running_total:,.2f}")

    # Allow the user to leave the program if so desired 😢
    elif action == "5":
        break

    # If te user enters a number outside of 1-5, have them try again
    else:
        print("Please choose a valid option.")

# A common curtesy
print("\nThank you! Goodbye.")







#Look this logic up

# try:
#     ...
# except:
#     ...