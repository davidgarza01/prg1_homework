'''
According to pep8 standard,
class names use PascalStyle

variable names are snake_case
'''

class Dog:
    def __init__(self, initial_name, age=0):
        self.name = initial_name
        self.age = age 
        pass

    def speak(self):
        print(self.name + " says Rrrrrrruuufffff")

    def change_name(self,newname):
        self.name = newname

    def calculate_dog_years(self):
        return self.age * 7

    def walk(self,xdiff,ydiff):
        self.x += xdiff
        self.y += ydiff

    def fetch(self,ballx,bally):
        x = self.x
        y = self.y
        self.walk(x + ballx, y + bally)
        self.walk()

    def celebrate_birthday(self):
        self.age += 1 
        print("Happy brithday" + self.name)



fido = Dog("fido",3)
fido.speak()
fido.change_name("Remmy") 
fido.speak()
print(fido.age)

rex = Dog("Rex",0)
rex.speak()
fido.speak()
print(rex.age)

thor = Dog("thor",11)
thor.speak()
print(thor.age)
