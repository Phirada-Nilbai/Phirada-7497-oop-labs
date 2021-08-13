sum = 0
count = 0
end_input = False
while not end_input:
    try:
        n = int(input(f"Enter an integer:"))
        if n <= 0 :
            print(f"Average is {avg}")
            break
        sum = sum + n
        count = count + 1
        avg = sum / count

    except ValueError :
        print("Please enter vaild integer")

