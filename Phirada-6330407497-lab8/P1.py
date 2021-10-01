#Phirada Nilbai 633040749-7 P1
class Rectangle:

    def __init__(self,width,height=0) :
        self.width = width
        self.height = height

    def __str__(self):
        return f"This rectangle has width as {self.width} height as {self.height} "

    def get_width(self):
        return self.width

    def set_width(self,widht):
        self.width = widht

    def get_height(self):
        return self.height

    def set_height(self,height):
        self.height = height

if __name__ =='__main__':
    rect1 = Rectangle(3,4);
    print(rect1);
    print(f"Width is {rect1.get_width()}")
    rect1.set_height(5)
    print(f"Height is {rect1.get_height()}")
