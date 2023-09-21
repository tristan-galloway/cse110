"""

Tristan Galloway
CES 110
Brother Keers
File: id_badge

"""
# This will collect the users name, contact info, and job information
first = input("What is your first name? ")
last = input("What is your last name? ")
email = input("What is your email address? ")
phone = input("What is your mobile phone number? ")
job = input("What is your job title? ")
id_num = input("What is your ID number? ")

# This will collect additional info about the user to better understand their demographic and skill level.
hair = input("What is your hair color? ")
eye_color = input("What color are your eyes? ")
start_month = input("What month did you start your job? ")
training = input("Do you have training, yes or no? ")

# This will reformat the users input to correct capitalization to the correct format for the badge
dash = "-"
first = first.capitalize()
last = last.upper()
email = email.lower()
job = job.title()
hair = hair.title()
eye_color = eye_color.capitalize()
start_month = start_month.capitalize()
training = training.capitalize()

# print the input of the user in a badge format
print("\nThe ID Card is:")

print(f"{dash * 40}")

print(f"{last}, {first}")
print(f"{job}")
print(f"ID: {id_num}\n")

print(f"{email}")
print(f"{phone}\n")

print(f"Hair: {hair:<23} Eyes: {eye_color}")
print(f"Month: {start_month:<22} Training: {training} ")

print(f"{dash * 40}")