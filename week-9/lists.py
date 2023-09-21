"""

student: tristan galloway
teacher: brother keers
file: lists.py
assignment: Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

"""

friends = []
friend = ""

print('Follow the prompts. When you\'re done, type "end"')


while friend != "end":
    # Ask user for their friends names
    friend = input("Type the name of a friend: ").lower()
    # If the user types the key word end, don't add it to the list
    if friend != "end":
        friends.append(friend)

# Return to the user their list of friends.
print(f"\nYour friends are: ")
for i in friends:
    print(f"{i.capitalize()}")
