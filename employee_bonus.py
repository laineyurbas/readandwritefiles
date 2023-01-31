import csv

infile = open("EmployeePay.csv", "r")
file2 = csv.reader(infile, delimiter=",")
for a in file2:
    print(a[1], a[2], a[3], a[4])
infile.close
