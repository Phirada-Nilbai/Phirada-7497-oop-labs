#Phirada Nilbai
#ID 633040749-7


def get_float(arg):
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            number = float(input(f"Enter {arg} floating point number:"))
            return number
        except ValueError:
            print("Please enter a valid floating point number")


def add():
    n1 = get_float("the first")
    n2 = get_float("the second")
    oper = input("Please enter an operator:")
    while True :
        if oper == '+':
            answer = n1 + n2
            print(f' {n1} {oper} {n2} = {answer}')
            break
        elif oper == '-':
            answer = n1 - n2
            print(f' {n1} {oper} {n2} = {answer}')
            break
        elif oper == '*':
            answer = n1 * n2
            print(f' {n1} {oper} {n2} = {answer}')
            break
        elif oper == '/':
            if  n2 == 0:
                print("Can not device by zero")
                break
            else:
                answer = n1 / n2
                print(f' {n1}{oper}{n2} = {answer}')
                break
        else:
            print("Unknow operator")
            break


if __name__ == "__main__":
    add()
