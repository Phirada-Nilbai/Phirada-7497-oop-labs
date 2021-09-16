#Phirada Nilbai 633040749-7
class Cat:


    def __init__(self, name, color):
        self.name = name
        self.color = color


    def get_num_legs():
        return f"4"


    def get_owner_name():
        return f"Lalisa Manobal"


    def print_info(self):
        print (f'Cat name is {self.name} and its color is {self.color}')


if __name__ == '__main__':
    leo = Cat("Leo","brown")
    luca = Cat("Lily","white")
    leo.print_info()
    luca.print_info()
    print(f"The number of legs all cats is {Cat.get_num_legs()}")
    print(f"The owner of these cats is {Cat.get_owner_name()}")
