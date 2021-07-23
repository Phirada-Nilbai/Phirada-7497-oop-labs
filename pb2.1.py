lst = input("Enter positive number:")
data = lst.split()
print("You enterd ",lst)
sum = 0
for x in data :
	sum += float(x)
avg = sum/len(data)
print("Average of the list =",avg)
