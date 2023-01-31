import csv

infile = open("EmployeePay.csv", "r")
file2 = csv.reader(infile, delimiter=",")
next(file2)
for item in file2:
    print("First Name is", item[1])
    print("Last Name is", item[2])
    print("Salary amount $" + item[3])
    bonusamt = int(item[3]) * float(item[4])
    total = int(item[3]) + (bonusamt, 2)
    print("Bonus amount $" + str(bonusamt, 2))
    print("Total amount $" + str(total))
    input()
infile.close()
