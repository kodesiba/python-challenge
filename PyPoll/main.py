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

    for row in csvreader:
        voters += 1
        candidate = row[2]
        if candidate not in candidates:
            candidatecounter += 1
            candidates.append(candidate)
            candidatevotes.append(1)
        else:
            currentcandidate = candidates.index(candidate)
            candidatevotes[currentcandidate] += 1


for i in range(len(candidates)):
    voterpct = round(candidatevotes[i]/voters*100,3)
    candidatevotepercent.append(voterpct)
    

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