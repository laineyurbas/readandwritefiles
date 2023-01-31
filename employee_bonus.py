import csv

infile = open("EmployeePay.csv", "r")
csvfile = csv.reader(infile, delimiter=",")
for a in csvfile:
    print(a[1], a[2], a[3], a[4])
infile.close
