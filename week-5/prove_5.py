"""

student: tristan galloway
teacher: brother keers
file: prove_5.py
task: In a text-based adventure game, the user is presented a scenario with different options. Depending on the option they choose, they have different consequences, which in turn present different choices for the next action.

"""
import random
import colorama
from colorama import Fore

# Set default win condition value
win_condition = False

# Start telling the story and ask for the first choice
choice = input("It's the year 2076 and zombies have flooded the world. You are walking throug dark city streets and find two items: a GUN and a KATANA. Which one do you want to pick up? ").upper()

# show the correct scenario based on the users choice: if-elif-else
if choice == "KATANA":  
    # keep telling the story and have the user make another choice
    choice = input("\nYou pick up the katana and hear the hords coming for you. Do you RUN from them, HIDE in a nearby building, or stay to HOLD your ground? ").upper()

    if choice == "RUN":
        print("\nYou made it out alive, zombies are slow. Why wouldn't you run? Well done survivor.")
        win_condition = True
    elif choice == "HIDE":
        print("\nYou duck into the building and find a counter top to hide behind. The zombies block the entrance and start swarming in. You've put yourself in a stupid position and are eaten alive.")
    elif choice == "HOLD":
        print("\nYou unsheeth your katan. As the Zombies approach you start picking them off. You kill 1, 2, 3. Your arms become weak as you continue to end them. They over powered you and feast on you.")
    else:
        print("\nYou froze in fear and were mauled by zombies!")


# if they choose gun have it randomly chooses each time whether or not the user will have ammo
elif choice == "GUN":
    # creativity assignment, learned how to use randint to create a ammo variable that will then change the possible scenarios.
    ammo = random.randint(0, 15)
    if ammo == 0:
        print("You aren't very lucky, the hoards devour you.")
    else:
        choice = input(f"\nYou pick up the glock 19 and check it's mag. You have {ammo} rounds. Do you open FIRE on the zombies, or RUN and find a building to fortify yourself in? ").upper()
        if choice == "FIRE":
            choice = input(f"\nYou start shooting, and take down {(ammo / .40):.0f} of them. Unfortunately, there are too many of them to take on right now, do you RUN or LOOK in a nearby building for another weapon? ").upper()
            if choice == "RUN":
                print("\nYou quickly turn and start running. A helicopter flies over and sees the hordes chasing you. They drop a rope to you and you escape with them.")
                win_condition = True
            elif choice == "LOOK":
                print("\nYou go into an adjacent building and begin searching. You can't find anything and hear the hords coming, but it's too late. They overwhelm you and end your life.")
            else:
                print("\nYour hesitation cost you your life.")
        elif choice == "RUN":
            print("\nYou find a nearby building and bolt the door. This saves you enough time to wait for others to find you. You are extracted and make it out alive.")
            win_condition = True
        else:
            print("\nYour hesitation cost you your life.")

else:
    print("\nYour hesistation cost you your life.")

#Let the user know the game is over
if win_condition:
    print(Fore.GREEN + "GAME OVER" + Fore.RESET)
else:
    print(Fore.RED + "GAME OVER" + Fore.RESET)