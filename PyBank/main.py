import csv
import os

#create path to data
csvpath = os.path.join("resources","budget_data.csv")

#initialize cumulative variables
months = 0
netamount = 0
maxup = 0
maxdown = 0

#read in data
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        months += 1
        netamount += int(row[1])
        if int(row[1])> maxup:
            maxup = int(row[1])
            maxupmonth = row[0]
        
        if int(row[1])<maxdown:
            maxdown = int(row[1])
            maxdownmonth = row[0]

avgchg = round(netamount/months,2)

print("Financial Analysis")
print("------------------")
print("Total Months: "+str(months))
print("Total: $"+str(netamount))
print("Average  Change: $"+str(avgchg))
print("Greatest Increase in Profits: "+maxupmonth+" $"+str(maxup))
print("Greatest Decrease in Profits: "+maxdownmonth+" $"+str(maxdown))