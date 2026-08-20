import random

class Key:
    iden = 0
    broken = False

    def __init__(self):
        self.iden = random.randint(1,10)

    def getIden(self):
        return self.iden

    def brake(self):
        self.broken = True

    def isBroken(self):
        return self.broken