"""

student: tristan galloway
teacher: brother keers
file: update.py
assignment: Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."

"""

# Create a list for the users shopping cart to be added to later
cart = []

# Ask the user to add items to their shopping cart
while True:
    items = input("What item would you like to add to your cart? ")
    
    # When the user types quit continue to the next loop
    if items.lower() == "quit":
        break
    
    cart.append(items)
    

while True:

    # Show the cart to the users with 0 based index numbers
    # 02.
    for i, item in enumerate(cart):
        print(f"[{i}] {item}")

    # Ask the user if they wnt to edit the cart
    answer = input("Would you like to edit the cart? (yes/no) ")

    # If the user said no then break out of the loop.
    if answer.lower() == "no":
        break

    # Ask the user for the index they would like to edit.
    index = int(input("What item do you want to change? (number) "))

    # Ask the user for the new item. 
    new_item = input("What is the new item? ")

    # Update the cart.
    cart[index] = new_item