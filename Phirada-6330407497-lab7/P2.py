#Phirda NIlbai 633040749-7
class Numbers:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


    def display_factors(self):
        if self%2 == 0 :
            return (f'Factor of {self} is {self/2} and {self/2}')
        else :
            return (f'Factor of {self} is {int((self/2)-0.5)} and {int((self/2)+0.5)}')


    def is_valid_divisor(self):
        if self == 0 :
            return (f'{self} is not a valid divisor')
        else :
            return (f'{self} is a valid divisor')


if __name__ == '__main__':
    print (f'2 + 3 is {Numbers(2,3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
