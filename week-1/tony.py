"""

File: hello.py
Author: Tristan Galloway

Purpose: Ask for their name, if it happens to be Tony... wreck them for it

"""

name = input("What's your name? ")
guy = "Tony"

if name == guy:
    print("F*ck you Tony!")
else:
    print(f"Hello {name}!")

# f declares it as a formatted statemnet and will allow me to use {} to have it print variables