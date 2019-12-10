import csv
import os

#create path to data
csvpath = os.path.join("resources","budget_data.csv")

#initialize cumulative variables
months = 0
netamount = 0
maxup = 0
maxdown = 0
previousrow = 0
totalchg = 0

#read in data
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        #calculate variables
        months += 1
        netamount += int(row[1])
        profitchange = int(row[1]) - previousrow
        totalchg += profitchange

        #check for max increase
        if profitchange> maxup:
            maxup = profitchange
            maxupmonth = row[0]
        
        #check for max decrease
        if profitchange<maxdown:
            maxdown = profitchange
            maxdownmonth = row[0]
        
        #set previous row value
        previousrow = int(row[1])

#calculate average change
avgchg = round(totalchg/months,2)
print(totalchg)

#print out results
print("Financial Analysis")
print("------------------")
print("Total Months: "+str(months))
print("Total: $"+str(netamount))
print("Average  Change: $"+str(avgchg))
print("Greatest Increase in Profits: "+maxupmonth+" $"+str(maxup))
print("Greatest Decrease in Profits: "+maxdownmonth+" $"+str(maxdown))