#Phirada Nilbai
#ID 633040749-7
#P5LAB3
def compute_sum_positive_odd_numbers():
    n = list(map(int,input("Enter numbers in the list:").strip().split()))
    total_positive_nums = list(filter(lambda n:n>0,n))
    odd_number = sum(filter(lambda x: x%2!=0, total_positive_nums))
    print(odd_number)
if __name__ == '__main__':
    compute_sum_positive_odd_numbers()
