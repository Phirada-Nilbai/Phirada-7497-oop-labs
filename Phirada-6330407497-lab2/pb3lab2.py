#Phirada Nilbai 633040749-7
def add_number_to_list():
    global num_list
    global num_list1
    num_list = [1, 2, 3, 4, 5]
    num_list1 = [1, 2, 3, 4, 5]
    print(f'Before adding an integer, the list is {num_list}')
    f = int(input("Please enter a number to add to list:"))
    num_list.append(f)
    print(f'After adding an integer {f}, the list is{num_list}')


def replace_number_in_list():
    print(f'Finding a number to replace in the list{num_list}')
    f = int(input("Enter a number to find:"))
    index = num_list.index(f)
    get_replace = int(input("Enter a number to replace:"))
    num_list[index] = get_replace
    print(f'After replacing {f} with {get_replace}, the new list is{num_list}')


def remove_number_in_list():
    print(f'Finding a number to replace in the list{num_list}')
    f = int(input("Enter a number to remove:"))
    num_list.remove(f)
    print(f'After remove {f}, the list is {num_list}')


if __name__ == '__main__':
    add_number_to_list()
    replace_number_in_list()
    remove_number_in_list()
