def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def get_int():
    while True:
        try:
            n = int(input("Enter a positive integer:"))
            if n <= 0:
                print("Please enter an integer that non-negative")
                break
            else :
                print(f"factorial of {n} is {factorial(n)} ")

        except ValueError:
            print("Please enter a valid integer")
            break



if __name__ == "__main__":
    get_int()
