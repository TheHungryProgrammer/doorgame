from key import Key

class Door: 
    isOpen = False  # Default all doors to being closed
    isLocked = False # Default all doors to unlocked (Useful for logic later)
    doorcolor = ""  # Default string value to nothing, change later on door init
    lock = 0        # Default door key code to 0, key randomizer chooses 1-10, it will never choose the unlocked door's combo
    hasTreasure = False # Is this our treasure door? Changed after all 3 doors are compiled.
    


    def __init__(self, color, lock):
        if(lock):
            self.isLocked = lock    # If the door is locked, we want it change its state
            self.theKey = Key()
            self.lock = self.theKey.getIden()
        self.doorcolor = color  # Make sure we know the door color

    def playerOpen(self):
        if(self.getState()):
            print("The handle rattles, the " + self.doorcolor + " door is locked.")
            return False
        else:
            self.isOpen = True
            print("The " + self.doorcolor + " door opens...")
            if(self.getTreasure()):
                return True
            else:
                return False

    def hintOpen(self):
        if(self.getState()):
            print("The handle rattles, the " + self.doorcolor + " door is locked.")
        else:
            self.isOpen = True
            print("The " + self.doorcolor + " door opens and reveals nothing")
            
    def getState(self):
        return self.isLocked

    def getOpen(self):
        return self.isOpen

    def getKey(self):
        return self.theKey

    def getColor(self):
        return self.doorcolor

    def getTreasure(self):
        if(self.hasTreasure):
            print("You found the treasure!")
            return True
        else:
            print("and reveals nothing!")
            return False

    def setTreasure(self):
            self.hasTreasure = True

    def unlock(self, thisKey):
            if(self.theKey == thisKey):
                self.isLocked = False
                print("The door unlocks")
                return True
            else:
                thisKey.brake()
                print("The key breaks in the lock. Game Over")
                return False

    #— the new central method. Internally handles, in order: "already open → return a lose result," "locked → try unlock(player_key)," 
    # "open the door," "check treasure." Returns something like a result object, enum, or simple string/tuple ("lose_already_open", 
    # "win", "lose_empty", "key_broke") rather than printing directly. This is what replaces the copy-pasted logic across your three 
    # match cases in main.py.
    def attemptOpen(self, player_key):
        if(self.getOpen()):
            print("Door was already open, and nothing was inside. You lose.")
            return False
        if(self.getState()):
            if(self.unlock(player_key)):
                return self.playerOpen()
            else:
                return False
        else:
            return self.playerOpen()
                

