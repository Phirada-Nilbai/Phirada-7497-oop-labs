import csv

with open("numbers.csv","w") as f:
     w = csv.writer(f)
     w.writerows([[2,4,6],[3,7,5],[8,9,7]])

with open("numbers.csv", "r")as fd:
    with open("numbers2.csv", "w",) as f2:
          rows = csv.reader(fd)
          w2 = csv.writer(f2)
          for row in rows:
               row.sort(reverse = True)
               #dont have average
               print (row)
               w2.writerow(row)
