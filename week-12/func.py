# Function Crash Course

def main():

    intro()
    room_1()

def intro():
    print("EPIC Intro....")

def room_1():
    print("room 1...")
    choice = input("[1] or [2]? ")

    if choice == "1":
        room_2
    elif choice == "2":
        room_3()
    else:
        print("Bad!1")
        room_1()

def room_2():
    print("Room 2")
    win()

def room_3():
    print("Room 3")
    game_over()

def win():
    print("Winner winner chicken dinner!")

def game_over():
    print("Game over. Git gud!!")