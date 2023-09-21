#           0    1    2    3    4
letters = ["P", "N", "Z", "J", "K"]

# r = range(0, 20)
# print(r)

while len(letters) < 5:
    letter = input("Please give me a letter: ").upper()
    letters.append(letter)

for i in range(len(letters)):
    print(f"{i + 1}. {letters[i]}")

for i, val in enumerate(letters):
    print(f"{i + 1}. {val}")

# "..." = "pass"

# if "continue" is run it will restart the loop and check if the statement is true or false again