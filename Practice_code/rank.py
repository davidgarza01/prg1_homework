class rank():
    def __init__(self):
        self.values = {
            "Ace" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "10" : 10,
            "Jack" : 11,
            "Queen" : 12,
            "King" : 13,
        }
    def validate ( self, face_value):
        if(face_value in self.values):
            return True
        else: 
            return False