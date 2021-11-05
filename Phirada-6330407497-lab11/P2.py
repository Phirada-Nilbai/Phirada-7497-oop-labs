import re

def split_str():
     word_list = [re.split('[ ]', s) for s in lst]
     print (word_list)


if __name__ == "__main__":
     lst = ["mana mana@kku.ac.th 043-222-3333",
         "manee manee@kku.ac.th. 043-888-9999"]
     split_str()
