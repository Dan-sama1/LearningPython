class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    #REUSING THE __init__ function in our Rectangle class
    def __init__(self,length, width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self,length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())