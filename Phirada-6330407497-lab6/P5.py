with open("word.txt", "r") as read_file:
    for line in read_file:
        str = line.split()
        print(str)
file = open("word.txt")
data = file.read()
words = data.split()
print('Threre are',len(words),'word in file word.txt')
