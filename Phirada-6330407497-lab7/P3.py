#Phirada Nilbai 633040749-7
import math
class Circle():


    def __init__(self,radius):
        self.radius=radius


    def area(self):
        return math.pi*(math.pow(self.radius,2))


    def perimeter(self):
        return 2*math.pi*self.radius


if __name__ == '__main__':
    try :
        r = float(input("Enter a radius: "))
        obj = Circle(r)
        print(f'The circle with radius {r} has the area as',round(obj.area(),2))
        print(f'and the perimeter as',round(obj.perimeter(),2))
    except ValueError :
        print("Please enter a valid floating-point number for the cricle radius")
