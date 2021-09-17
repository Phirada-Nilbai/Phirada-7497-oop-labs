#Phirada Nilbai
#ID 633040749-7
#P1LAB3
def guess_num():
  import random
  secret=random.randint(1,10)
  MAX_NUM_GUESSES = 5
  tries= MAX_NUM_GUESSES
  while tries > 0:
    guess=int(input("Enter an integer to guess:" ))
    if guess==secret:
      print("Congrats that you guess the number correctly")
      break
    elif guess>secret:
      tries = tries - 1
      print("Try a lower number")
      print(f"You have {tries} guesses remaining")
    else:
      tries = tries - 1
      print("Try a higher number")
      print(f"You have {tries} guesses remaining")

if __name__ == '__main__':
  guess_num()


