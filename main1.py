from door import Door as door
from key import Key as key
import random

class Main:
    playerKey = key()

    print(
          "Hello, and welcome to the door game.\n"
          "In this game there are Three Doors: A Red Door, a Blue Door, and a Green Door...\n"
          "Behind one of the doors is a treasure, but beware.\n"
          "Two of the doors are locked, One is not.\n"
          "You have one key to one of the locked doors.\n"
          "At the start, you will be allowed to unlock a door or pass. Then I will attempt to open a door without the treasure.\n"
          "If I cannot, you will hear the door rattle.\n"
          "The objective is not to find the treasure, but to figure out where it is. Guess right and win, guess wrong and so long chum\n"
          )

    answer = input("Would you like to play? [y]/[n]\n").lower()
    while answer == "y":
        redDoor = door("red",random.choice([True,False]))
        # If random red door lock state, if locked then random blue door lock state
        # If Red & Blue are Locked, then Green must be Unlocked (default, no line needed)
        # If Red is Locked, and Blue is Unlocked, Green must be Locked
        # If red is Unlocked, then Blue and Green must be Locked.
        if(redDoor.getState()):
            blueDoor = door("blue", random.choice([True,False]))
            if(blueDoor.getState()):
                greenDoor = door("green", False)
            else:
                greenDoor = door("green", True)
        else:
            blueDoor = door("blue", True)
            greenDoor = door("green", True)
        myList = [redDoor,blueDoor,greenDoor]

        randDoor = random.choice(myList)    # Randomly determine which door has the treasure
        randDoor.setTreasure()              # Assign the door as the treasure holder

        if(randDoor.getState()):              # If the treasure door is locked, the player should have its key, 
            playerKey = randDoor.getKey()     
        else:                               # else give the player a random key
            newChoice = randDoor
            while newChoice == randDoor:
                newChoice = random.choice(myList)
            playerKey = newChoice.getKey()

        print(f"I have created three doors: [Red Door], [Blue Door], [Green Door] and placed a treasure behind one of them.\n")
        print(f"Here's a hint, I will attempt to open a door!")
        if(randDoor == redDoor):    # Attempt to open one of the non-treasure doors
            choice = random.choice([blueDoor, greenDoor])
        elif(randDoor == blueDoor):
            choice = random.choice([redDoor, greenDoor])
        else:
            choice = random.choice([blueDoor, redDoor])
        choice.hintOpen()

        finalChoice = input("Two Options left, which door do you choose?\n[Red Door]/[Blue Door]/[Green Door]\n")
        match finalChoice:
            case "red door":
                if(redDoor.getOpen()):            # if the player chooses an already open door, they should lose to pure idiocy
                    print(f"You chose the open door with nothing. You lose")
                    answer = input("Play again? [y]/[n]\n").lower()
                    continue
                else:
                    if(redDoor.isLocked):       # Otherwise they should attempt to open it
                        redDoor.unlock(playerKey)
                redDoor.playerOpen()
                redDoor.getTreasure()
            case "blue door":
                if(blueDoor.getOpen()):
                    print(f"You chose the open door with nothing. You lose")
                    answer = input("Play again? [y]/[n]\n").lower()
                    continue
                else:
                    if(blueDoor.isLocked):
                        blueDoor.unlock(playerKey)
                blueDoor.playerOpen()
                blueDoor.getTreasure()
            case "green door":
                if(greenDoor.getOpen()):
                    print(f"You chose the open door with nothing. You lose")
                    answer = input("Play again? [y]/[n]\n").lower()
                    continue
                else:
                    if(greenDoor.isLocked):
                        greenDoor.unlock(playerKey)
                greenDoor.playerOpen()
                greenDoor.getTreasure()
        answer = input("Would you like to play again? [y]/[n]\n")
    print("Thank you for playing!")