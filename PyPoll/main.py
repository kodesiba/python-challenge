import csv
import os

#create path for csv
csvpath = os.path.join("resources","election_data.csv")

#initialize cumulative variables
voters = 0
candidatecounter = -1
candidates = []
candidatevotes = []
candidatevotepercent = []
winningvotes = 0

#read in data
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #iterate through csv rows
    for row in csvreader:
        #calculate voters and create local vars
        voters += 1
        candidate = row[2]

        #check to see if new candidate and update items accordingly
        if candidate not in candidates:
            candidatecounter += 1
            candidates.append(candidate)
            candidatevotes.append(1)
        else:
            currentcandidate = candidates.index(candidate)
            candidatevotes[currentcandidate] += 1

#summarize candidate data
for i in range(len(candidates)):
    voterpct = round(candidatevotes[i]/voters*100,3)
    candidatevotepercent.append(voterpct)
    
#print results
print("Election Results")
print("----------------")
print("Total Votes: "+str(voters))
for p in range(len(candidates)):
    print(candidates[p]+": "+str(candidatevotepercent[p])+"% ("+str(candidatevotes[p])+")")
    if candidatevotes[p] > winningvotes:
        winningvotes = candidatevotes[p]
        winner = candidates[p]
print("----------------")
print("Winner: "+winner)
print("----------------")

#create output file
outfilepath = os.path.join("output","output.txt")
outfile = open(outfilepath,"w")

#write file text
outfile.writelines("Election Results")
outfile.writelines("\n----------------")
outfile.writelines("\nTotal Votes: "+str(voters))
for p in range(len(candidates)):
    outfile.writelines("\n"+candidates[p]+": "+str(candidatevotepercent[p])+"% ("+str(candidatevotes[p])+")")
    if candidatevotes[p] > winningvotes:
        winningvotes = candidatevotes[p]
        winner = candidates[p]
outfile.writelines("\n----------------")
outfile.writelines("\nWinner: "+winner)
outfile.writelines("\n----------------")