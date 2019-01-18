import random 
class dice(): 
    def __init__(self):
        self.sides = {
            "1st" : 1,
            "2nd" : 2,
            "3rd" : 3,
            "4th" : 4,
            "5th" : 5,
            "6th" : 6,
        }

    def roll(self):
        roll_dice = random.randint(self.sides)


