#Phirada Nilbai 633040749-7
while True:
    try:
        temp_cel = float(input("Enter a temperature in celsius:"))
        temp_fah = (9/5) * temp_cel + 32
        print(temp_cel,"in celsius is:",temp_fah,"Fahrenheit")
        break
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
