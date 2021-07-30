#Phirada Nilbai 633040749-7
def Check_Vow(string, vowels):
	final = [each for each in string if each in vowels]
	print(final)

string = input("Enter the sentence:")
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);
