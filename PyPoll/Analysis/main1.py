import os
import csv

file = r'PyPoll\Resources\election_data.csv'

with open(file, 'r') as f:
    csvreader = csv.reader(f, delimiter=",")
    # Skip header row
    next(csvreader)

    total_votes = 0
    candidates_votes_count = {}

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Update vote count for the candidate
        if candidate_name in candidates_votes_count:
            candidates_votes_count[candidate_name] += 1
        else:
            candidates_votes_count[candidate_name] = 1

# Calculate percentage of votes each candidate won
candidates_percentage = {}
for candidate, votes in candidates_votes_count.items():
    percentage = (votes / total_votes) * 100
    candidates_percentage[candidate] = percentage

# Determine the winner
winner = max(candidates_votes_count, key=candidates_votes_count.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes_count.items():
    percentage = candidates_percentage[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
