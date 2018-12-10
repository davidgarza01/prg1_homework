class suit():
    def __init__(self):
        self.values = {
            "Hearts" : 0,
            "Spades" : 1,
            "Diamonds" : 2,
            "Clubs" : 3,
            "Invalid" : -1,
        }
        
    def validate(self, suit_value):
        if(suit_value in self.values):
            return True 
        else:
            return False