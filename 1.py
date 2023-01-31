import csv

infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")
csvfile = csv.reader(infile, delimiter=",")
next(csvfile)
outfile.write(
    "Full Name Country \n",
)
for list in csvfile:
    firstname = list[1]
    lastname = list[2]
    country = list[4]
    data = firstname + " " + lastname + ", " + country
    outfile.write(data + "\n")

infile.close()
