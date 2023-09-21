"""

student: tristan galloway
course: ces 110
teacher: brother keers
file: madlibs

"""

# Giving the user a prompt explaining what to do
print("\nPlease enter the following:\n")

# Asks user for the variables needed to fill in the blanks in the madlib
adjective_1 = input("Adjective: ")
noun_1 = input("Noun: ")
profession = input("profession: ")
verb_1 = input("Verb ending in -ing: ")
adjective_2 = input("Adjective: ")
noun_2 = input("Noun: ")
verb_2 = input("Verb: ")
adjective_3 = input("Adjective: ")



# Giving the user their finished madlib
print("\nYour story is:")

# Made this on chat GPT by asking it to make a one paragraph madlib
story = f""" 

Once upon a {adjective_1.lower()} time, there was a {noun_1.lower()} who wanted to become a {profession.lower()}. But 
unfortunately, every time they tried, they ended up {verb_1.lower()} themselves. One
day, they met a {adjective_2.lower()} {noun_2.lower()} who offered to {verb_2.lower()} them. Skeptical at first, the {noun_1.lower()} 
eventually agreed and to their surprise, they succeeded! From that day on, the {noun_1.lower()} 
became the most {adjective_3.lower()} {profession.lower()} in all the land.

"""

# Returning the finished madlib to the user
print(story)

# Asking the user for a review of the madlib experience.
rating = input("Thank you for using the Madlib app, would you like to leave a review? (yes or no) ")
rating = rating.lower()

# Taking the rating and wrapping up the loose ends by using an if else statement. Then giving a reward to the user for them taking time to take the survey
if rating == "yes": 
    scale_rating = input("On a scale of 1-5 how would you rate your experience? ")
    print(f"Thank you for taking the time to rate us! If you reach out to Brother Keers, he will send you $100. Enjoy your day!")
else:
    print("Wrong choice, good luck.")