#Phirada Nilbai
#ID 633040749-7
#P4LAB3
word = input("Enter a string:")
output_list=[i for i in word]
print("chars are",(output_list))

output_list2=[i for i in word if i in 'aAeEiIoOuU']
lst = [x.upper() for x in output_list2]
print(lst)
