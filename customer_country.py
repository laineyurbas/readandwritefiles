import csv

infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")
file2 = csv.reader(infile, delimiter=",")
next(file2)
outfile.write(
    "Full Name Country \n",
)
for item in file2:
    a = item[1]
    b = item[2]
    c = item[4]
    output = a + " " + b + ", " + c
    outfile.write(output + "\n")

infile.close()
