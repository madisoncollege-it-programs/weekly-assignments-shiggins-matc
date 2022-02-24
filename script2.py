#!/usr/bin/env python3
# A Silly text adventure by: Sean Higgins

print("""You enter a dark room with three doors.
Do you go through door #1, door #2 or door #3?""")

door = input("-> ")

# == Door Number 1 logic ===================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Challenge the bear to a rap battle to win his cheese cake.")

    # == Bear logic ========================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    elif bear == "3":
        print("3) The bear is jealous of your skills and rips you in half. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door number 2 logic ===================
elif door =="2":
    print("You stare into the endless abyss at Cthulhu's domain. \n")
    print("Cthulhu offers you a variety of items on a large platter, do you take one?")

    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # == Insanity logic ====================
    insanity = input("-> ")

    if insanity =="1" or insanity =="2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print(" Cthulhu's gaze drives you mad and insanity rots your eyes into a pool of muck.")
        print(" Good job!")
# == Door number 3 logic ===================

elif door =="3":
    print("You see a little old woman knitting, who tells you to fetch her more yarn. \n")
    print("Do you \n")
    print("1. Grab the yarn from the corner.")
    print("2. Grab the yarn off the table in the middle of the room.")
    print("3. Ignore the request.")

    # == Old lady logic ====================
    doom = input("-> ")

    if doom == "1":
        print("With your focus on the yarn the old woman stabs you while your back is to her.")
    elif doom == "2":
        print("The floor falls out from under you and you are trapped in a pit. Good job!")
    elif doom == "3":
        print("The woman tells you to leave if you are not going to be helpful.\n  You turn around and walk out the door.")
    else:
        print("The woman disappears into a mysterious cloud of smoke.")

else:
    print("You did not select a door??? Good Call :)")
