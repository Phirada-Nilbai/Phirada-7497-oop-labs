import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
charecters = lower + upper + digits + symbols
temp = random.sample(charecters,9)
password = ''.join(temp)
print("Random password is:",password)
