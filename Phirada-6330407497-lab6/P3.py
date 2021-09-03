try :
    with open('kipchonge.txt', 'r') as filename:
        read_data = filename.read()
        read_file = input("Enter file name to read:")
        textappend = input("Enter text to append:")
        write_file = input("Enter file name to write:")
        newQ = []
        if read_file == 'kipchonge.txt':
            newQ.append(textappend)
            print(read_data)
            print(newQ)
        else :
            print("not have file")
    with open(write_file, 'w') as filename:
        data = {}

except ValueError :
    print("have not file")
