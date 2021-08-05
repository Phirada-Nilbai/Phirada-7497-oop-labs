#Phirada Nilbai
#ID 633040749-7
#P2LAB3
def fruits_srot_upper():
    newList = []
    fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
    print("The fruits are ['Grapefruit', 'Longan', 'Orange', 'Apple', 'Cherry']")
    print("After converting fruits to uppercase letters, fruits are")

    for count,ele in enumerate(fruits,1):
	    print (count,ele.upper())
    print("After sorting fruits, frutis are")

    fruits.sort()
    for fruit in fruits:
        newList.append(fruit.upper())
    print(newList)

if __name__ == '__main__':
    fruits_srot_upper()
