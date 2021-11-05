import re

text = input("Enter text:")
pattern = input("Enter pattern:")
result =  re.findall(pattern,text)
position = text.find(pattern)

if result :
     print (f'Found {pattern} in {text} at {position}')
else :
     print (f'Cannot find {pattern} in {text}')
