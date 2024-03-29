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

    #iterate through csv rows
    for row in csvreader:
        #check if first month, if so set previous row to current row to nullify change calculation
        if months==0:
            previousrow = int(row[1])

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
        
        #set previous row value for next calculations
        previousrow = int(row[1])

#calculate average change
avgchg = round(totalchg/(months-1),2)

#print out results to terminal
print("Financial Analysis")
print("------------------")
print("Total Months: "+str(months))
print("Total: $"+str(netamount))
print("Average  Change: $"+str(avgchg))
print("Greatest Increase in Profits: "+maxupmonth+" $"+str(maxup))
print("Greatest Decrease in Profits: "+maxdownmonth+" $"+str(maxdown))

#create output file
outfilepath = os.path.join("output","output.txt")
outfile = open(outfilepath,"w")

#write file text
outfile.writelines("Financial Analysis")
outfile.writelines("\n------------------")
outfile.writelines("\nTotal Months: "+str(months))
outfile.writelines("\nTotal: $"+str(netamount))
outfile.writelines("\nAverage  Change: $"+str(avgchg))
outfile.writelines("\nGreatest Increase in Profits: "+maxupmonth+" $"+str(maxup))
outfile.writelines("\nGreatest Decrease in Profits: "+maxdownmonth+" $"+str(maxdown))