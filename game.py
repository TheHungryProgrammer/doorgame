from door import Door as door
from key import Key as key
import random

class Game():

    # — sets up empty state: door list, treasure door reference, player key reference. Doesn't run any game logic yet, just prepares the object.
    def __init__(self):
        self.doorList = []
        self.treasureDoor = door("purple", False)
        self.playerKey = key() 
    
    # — owns the red→blue→green cascading lock logic. Creates the three doors, guarantees the "exactly one unlocked" rule, and stores them in self.doors. Replaces the inline block currently in your while loop.
    def setup_doors(self):      
        self.redDoor = door("red",random.choice([True,False]))
        # Create random red door lock state, if locked then random blue door lock state
        # If Red & Blue are Locked, then Green must be Unlocked
        # If Red is Locked, and Blue is Unlocked, Green must be Locked
        # If red is Unlocked, then Blue and Green must be Locked.
        if(self.redDoor.getState()):
                    self.blueDoor = door("blue", random.choice([True,False]))
                    if(self.blueDoor.getState()):
                        self.greenDoor = door("green", False)
                    else:
                        self.greenDoor = door("green", True)
        else:
            self.blueDoor = door("blue", True)
            self.greenDoor = door("green", True)
        self.doorList = [self.redDoor,self.blueDoor,self.greenDoor]

    # — picks the treasure door from self.doors, calls setTreasure() on it, stores the reference.
    def assign_treasure(self):  
        self.treasureDoor = random.choice(self.doorList)    # Randomly determine which door has the treasure
        self.treasureDoor.setTreasure()                # Assign the door as the treasure holder

    # — handles the "if treasure door is locked, give player its key; otherwise give a random other door's key" logic. 
    # Sets self.playerKey.
    def assign_player_key(self):
        if(self.treasureDoor.getState()):            # If the treasure door is locked, the player should have its key, 
                    self.playerKey = self.treasureDoor.getKey()     
        else:                               # else give the player a random key
            newChoice = self.treasureDoor
            while newChoice == self.treasureDoor:
                newChoice = random.choice(self.doorList)
            self.playerKey = newChoice.getKey()

    # — picks a non-treasure door (excluding self.treasureDoor, fixing the bug we found) and opens it. Replaces the if/elif/else block.
    def reveal_hint(self):
        print(f"I have created three doors: [Red Door], [Blue Door], [Green Door] and placed a treasure behind one of them.\n")
        print(f"Here's a hint, I will attempt to open a door!")
        choice = self.treasureDoor
        while(choice == self.treasureDoor):
             choice = random.choice(self.doorList)
        choice.hintOpen()
        

    # — handles the input() and match statement for the player's final door pick. Returns which door was chosen 
    # (or the door object itself), not print statements — keep this method about getting input, not resolving outcomes.
    def prompt_final_choice(self):
        finalChoice = input("Two choices left...[Red Door]/[Blue Door]/[Green Door]\n").lower()
        match finalChoice:
            case "red door":
                  return self.redDoor
            case "red":
                return self.redDoor
            case "blue door":
                  return self.blueDoor
            case "blue":
                return self.blueDoor
            case "green door":
                  return self.greenDoor
            case "green":
                 return self.greenDoor

    # — takes the door the player picked and delegates to that door's own logic (see Door.attempt_open below) to figure out win/lose/broken key, then handles the printed narrative result. This is where the three near-identical match cases in your current code collapse into one reusable path.
    def resolve_choice(self, chosen_door):
         if(chosen_door.attemptOpen(self.playerKey)):
              print("You Win!")
         else:
              print("You Lose!")

    # — orchestrates one full round by calling the above methods in order: setup → assign treasure → assign key → hint → prompt → resolve. This is the method that replaces the body of your current while loop.
    def play_round(self):
        self.setup_doors()
        self.assign_treasure()
        self.assign_player_key()
        self.reveal_hint()
        self.resolve_choice(self.prompt_final_choice())

    # — the outer loop. Prints the welcome message once, asks "would you like to play," and calls play_round() repeatedly while the answer is yes. This is the only method that should contain while and the replay prompt.
    def play(self):
        print(
                  "Hello, and welcome to the door game.\n"
                  "In this game there are Three Doors: A Red Door, a Blue Door, and a Green Door...\n"
                  "Behind one of the doors is a treasure, but beware.\n"
                  "Two of the doors are locked, One is not.\n"
                  "You have one key to one of the locked doors.\n"
                  "At the start I will attempt to open a door without the treasure.\n"
                  "If I cannot, you will hear the door rattle.\n"
                  "The objective is to find the treasure. Guess right and win!\n"
                  )
        answer = input("Would you like to play a game? [Yes]/[No]\n").lower()
        while answer == 'yes':
            self.play_round()
            answer = input("Would you like to play again? [Yes]/[No]\n").lower()