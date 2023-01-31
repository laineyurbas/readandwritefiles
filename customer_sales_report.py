import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")
csvfile = csv.reader(infile, delimiter=",")
# customerid = " "
next(csvfile)
outfile.write(
    "Customer ID, Total \n",
)
customerid = "250"
customertot = 0

for num in csvfile:
    if customerid != num[0]:

        # customertot = float(num[3]) + float(num[4]) + float(num[5])
        # data = num[0] + " , " + str(customertot)

        outfile.write(customerid + "\t\t\t" + str("%.2f" % customertot) + "\n")
        customerid = num[0]
        customertot = 0

    Total = float(num[3]) + float(num[4]) + float(num[5])
    customertot += Total

# data = num[0] + " , " + num[3]

outfile.write("261" + "\t\t\t" + str("%.2f" % customertot))
infile.close()
outfile.close()
