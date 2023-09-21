"""

File: favorite color
Author: Tristan Galloway

Purpose: To get a users favorite color and do it in a more normal way

"""

name = input("Hey there! What's your name? ")
# asking for the users name

color = input(f"It's nice to meat you {name}! I'd love to get to know you better. So obviously we'll start with the most important questions, what's your favorite color? ")
# asking user for favorite color

if color.lower() == "blue":
    print ("Blue is super pretty, especially light blues like the sky!")
elif color.lower() == "red":
    print ("I enjoy red, it's nice for late nights when you want a light that's gentle on your eyes.")
elif color.lower() == "green":
    print ("What are you, a hippie? Gross.")
elif color.lower() == "pink":
    print (f"Ah yes, a person of culture")
else:
    print ("That's a good choice!")
# gives unique responses if they say certain colors. if it's any other color give a generic response

print  ("Well we can pick this back up again next time. See you around!")
# the end, thank you for coming to my ted talk