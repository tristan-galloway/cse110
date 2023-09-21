"""

student: tristan galloway
teacher: brother keers
file: finding_list.py
assignment: Write a program to find the youngest person in the list.

"""

NAME_INDEX = 0
AGE_INDEX = 1

# Start our our min_age variable high so we can set it to lower numbers
min_age = 999999
# Keep track of the youngest persons name
min_name = ""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Go through each person in the list of people
for person in people:

    parts = person.split()

    # Sepparating name and age in the list
    name = parts[NAME_INDEX]
    age = int(parts[AGE_INDEX])

    # Check to see if this is the youngest person thus far
    if age < min_age:
        min_age = age
        min_name = name

    # Print all of the names and their ages
    print(f"{name}: {age}")

# Return the youngest age and name
print(f"The youngest in this data set is {min_name} and they are {age} years old.")