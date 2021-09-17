#Phirada Nilbai
#ID 633040749-7
#P6LAB3
n = int(input("Enter a integer:"))
l = [i for i in range(1,n+1)]
res = sum(map(lambda i : i * i, l))
print ("The sum of squares of list",l," is " + str(res))
