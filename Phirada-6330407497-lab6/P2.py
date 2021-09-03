try :
    with open('kipchonge.txt') as filename:
        read_data = filename.read()
        filename = input("Enter a file name:")
        print(read_data)
except Exception :
    print("have not file")

