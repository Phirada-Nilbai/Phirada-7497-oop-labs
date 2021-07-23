def compute_avg_list():
	sum = 0
	list = []
	while True:
		inputuser = int(input("Enter positive number:"))
		if inputuser < 0 :
			print("You enterd",list)
			average = sum/len(list)
			print("The average number of a list is %.1f" %average)
			break
		elif inputuser > 0 :
			sum += inputuser
			list.append(inputuser)

if __name__ == "__main__":
	compute_avg_list()
