import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")
file2 = csv.reader(infile, delimiter=",")
# customerid = " "
next(file2)
outfile.write(
    "Customer ID, Total \n",
)
customerid = "250"
customertot = 0

for num in file2:
    if customerid != num[0]:

        outfile.write(customerid + "\t\t\t" + str("%.2f" % customertot) + "\n")
        customerid = num[0]
        customertot = 0

    realtotal = float(num[3]) + float(num[4]) + float(num[5])
    customertot += realtotal

outfile.write("261" + "\t\t\t" + str("%.2f" % customertot))
infile.close()
outfile.close()
