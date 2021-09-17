#Phirada Nilbai 633040749-7

olympics2020_str = "Badminton: Thailand vs. Great Britain , Table Tennis: Thailand vs Japan"

if __name__ == '__main__':
    th = olympics2020_str.split(' ', 2)[1]
    vs = olympics2020_str.split(' ', 3)[2]
    bad_britain = olympics2020_str.split(' ', 4)[3]
    bad_britain2 = olympics2020_str.split(' ', 5)[4]
    jp = olympics2020_str.split(' ', 11)[-1]
print("For some olympic 2020 games of Thailand athletes: ")
print("For Badminton, the game is between", th, vs, bad_britain, bad_britain2)
print("For Table Tennis, the game is between", th, vs,jp)
