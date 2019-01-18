class shape():
    def __init__(self,sides,area,perimeter):
        self.sides = sides
        self.area = area
        self.perimeter = perimeter

        def display():
            print(self.sides, self.area,self.perimeter)


class oval():    
    def __init__(self,sides,area,perimeter):
        shape __init__(self,sides,area,perimeter)

class rectangle(shape):
    def __init__ (self,length, width):
        self.area = length * width
        self.sides = 4
        self.perimeter = 2*length + 2*width


class square(shape):
    def __init__(self,length):
        self.area = length * length
        self.sides = 4
        self.perimeter = length * self.sides 

o = oval(4,6,10)
s = square(10)
r = rectangle(4,10)
q = TimeoutError()

shapes = [o,s,r,q]
for shape in shapes:
    shape.display()
