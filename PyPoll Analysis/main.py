import os
import csv

electionCsv = os.path.join(os.getcwd(),'resources','election_data.csv')
totalVotes = 0
votespercanidate = {}
with open(electionCsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") to see the headers
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votespercanidate:
            votespercanidate[row[2]] = 1 
        else:
            votespercanidate[row[2]] += 1
print("Election Results")
print("-----------")
print("Total Votes:" + str(totalVotes))
print("-----------")            
for candidate, votes in votespercanidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
print("-------------------------") 

winner = max(votespercanidate, key=votespercanidate.get)
print(f"Winner: {winner}")
output = open("output.txt", "w")
output.write("Election Results")
output.write('\n')
output.write("-------------------------")
output.write('\n')
output.write("Total Votes: " + str(totalVotes))
output.write('\n')
output.write("-------------------------")
output.write('\n')

for candidate, votes in votespercanidate.items():
    output.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    output.write('\n')
output.write("-------------------------") 
output.write('\n')
output.write(f"Winner: {winner}")
output.write('\n')