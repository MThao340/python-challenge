import os
import csv

csv_path = os.path.join("PyPoll","Resources",'election_data.csv')

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    election_data = list(csvreader)
    
totalvotes = 0
candidates = []
candidate = []
candidate_list = []
candidate_votes = []
votes = []
vote_count = []
percentage = []
percentage_voted_list = []

for row in election_data[1:]:
    candidates.append(row[2])
    percentage = []
    winner = ""
    winner_count = 0
    highest_value = 0
    totalvotes = totalvotes + 1

if candidate not in candidates:
    candidates.append(candidates)
    votes.append(1)
else:
    index = candidates.index(candidate)
    votes[index] += 1

percentage_voted_list = [(votes[i] / totalvotes * 100) for i in range(len(candidates))]

winner_index = votes.index(max(votes))
winner = candidates[winner_index]

for i in range(len(candidate_list)):
    candidate = candidates[i]
    percentage = percentage_voted_list[i]
    vote_count = votes[i]

print("Election Results")
print("-------------------------")
print("Total votes: " + str(totalvotes))
print("-------------------------")
print(f"{candidates}: {percentage:.2f}% ({vote_count})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")
print("Winner: " + winner)


