#Phirada Nilbai
#ID 633040749-7
#P3LAB3
word = input("Enter a string:")
def split(word):
	return [char for char in word]
print("chars are",split(word))
print("The entered string is",(word),"and result of convert a vowel to uppercase is")

def Check_Vow(word, vowels):
	final = [each for each in word if each in vowels]
	print(final)

vowels = "AaEeIiOoUu"
Check_Vow(word.upper(), vowels);
