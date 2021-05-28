from .Dice_Class import Dice

class Player(Dice):
    def __init__(self, name):
        self.name = name
        self.dice = Dice()
        self.dice.roll()