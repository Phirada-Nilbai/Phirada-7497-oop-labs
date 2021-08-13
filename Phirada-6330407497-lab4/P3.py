#Phirada Nilbai
#ID 633040749-7
def get_int(arg):
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            number =int(input(f"Enter the number infected Covid19 cases for {arg} :"))
            if number >= 0:
                return number
            else :
                print(f"You can only enter a non-negative integer")
                continue
        except ValueError:
            print("Please enter a valid integer")
        finally:
            print("Stay healthy!")


def add():
    n1 = get_int("yesterday")
    n2 = get_int("today")
    result = int(((n2 - n1) * 100) / n1)
    print(f'The difference of number of new infected cases is {result:0.2f}%')


if __name__ == "__main__":
    add()
