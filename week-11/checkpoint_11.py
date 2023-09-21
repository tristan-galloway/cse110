"""

student: tristan galloway
teacher: brother keers
file: checkpoint_11
assignment: open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

"""

# Outdated way to code it
"""

book_file = open("books.txt", "r")

for line in book_file:
    print(line.strip())

book_file.close()

"""

# Current way
# Open the file books.txt and save it to a variable name book_file
with open("books.txt", "r") as book_file:
    # For each line in the books.txt print it on it's own line with all spacing surrounding the lines stripped off.
    for line in book_file:
        print(line.strip())