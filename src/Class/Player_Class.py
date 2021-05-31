from .Dice_Class import Dice
import random

class Player(Dice):
    def __init__(self, ai = False):
        self.ai = ai
        self.name = "" if not self.ai else "AI#"+str(random.randint(1000, 9999))
        self.dice = Dice()
        self.pv = 30
        self.status = None
        self.dmg = {}

    def set_name(self):
        self.name = input("> ")
    
    def set_status(self):
        self.status = self.dice.status
        self.dmg = {"magic": self.dice.magic+self.dice.stock} if self.dice.magic > self.dice.physic else {"physic": self.dice.physic+self.dice.stock}
        self.dice.stock = 0